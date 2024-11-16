from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

User = get_user_model()

class OnlineStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        if user.is_authenticated:
            user.is_online = True
            await self.update_user_status(user)

    async def disconnect(self, close_code):
        user = self.scope['user']
        if user.is_authenticated:
            user.is_online = False
            await self.update_user_status(user)



