# library_system/asgi.py

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import library.routing  # 导入您的应用路由

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            library.routing.websocket_urlpatterns
        )
    ),
})
