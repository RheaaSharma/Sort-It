from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'^$', consumers.CanyonConsumer.as_asgi()),
    re_path(r'^results/$', consumers.ResultConsumer.as_asgi()),

]