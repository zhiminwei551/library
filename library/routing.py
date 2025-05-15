# library/routing.py

from . import consumers
from django.urls import path

websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),  # 路由与 `student_home.html` 中的 WebSocket 路径一致
]
