from django.urls import path
from unimarket.consumers import OnlineStatusConsumer

ws_urlpatterns = [
    path('ws/online-status/', OnlineStatusConsumer.as_asgi()),
]