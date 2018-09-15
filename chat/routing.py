from django.conf.urls import url
from . import consumers


websocket_urlpatterns = [
    # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    url(r'^ws/chat/done/', consumers.ChatConsumer.done),
    url(r'^ws/chat/', consumers.ChatConsumer),
]
