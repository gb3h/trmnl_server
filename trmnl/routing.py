from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r"ws/preview", consumers.PreviewConsumer.as_asgi()),
]
