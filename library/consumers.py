import os
import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from openai import OpenAI

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("尝试建立 WebSocket 连接")
        # 不进行用户认证检查，允许所有连接
        self.room_group_name = 'chat_room'
        logger.info(f"加入房间 {self.room_group_name}")
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        logger.info("WebSocket 连接已接受")

    async def disconnect(self, close_code):
        logger.info("WebSocket 连接已断开")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        logger.info(f"接收到消息: {text_data}")
        data = json.loads(text_data)
        message = data.get('message', '')

        if not message:
            logger.warning("接收到空消息")
            return

        if len(message) > 1000:
            logger.warning("消息长度超过限制")
            await self.send(text_data=json.dumps({'message': '消息过长，请限制在1000字以内。'}))
            return

        # 调用大模型 API
        await self.get_model_response(message)

    async def get_model_response(self, user_message):
        """
        调用大模型 API 获取一次性回复
        """
        client = OpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )

        try:
            logger.info(f"调用 API: {user_message}")
            # 调用模型生成回复
            completion = client.chat.completions.create(
                model="qwen-plus",  # 使用的模型名称
                messages=[
                    {'role': 'system', 'content': 'You are a helpful assistant.'},
                    {'role': 'user', 'content': user_message}
                ]
            )

            # 获取模型的完整回复
            response = completion.choices[0].message.content
            logger.info(f"API 调用成功，返回内容: {response}")

            # 将响应发送回 WebSocket
            await self.send(text_data=json.dumps({
                'message': response
            }))

        except Exception as e:
            logger.error(f"API 调用失败: {str(e)}")
            await self.send(text_data=json.dumps({'message': f"发生错误：{str(e)}"}))
