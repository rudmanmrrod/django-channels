"""
Django Realtime Chat & Notifications
"""
## @package chat.consumers
#
# Consumer del web socket
# @version 1.0
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'chat',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'chat',
            self.channel_name
        )

    async def receive(self, text_data):
        # Send message to room group
        await self.channel_layer.group_send(
            'chat',
            {
                'type': 'chat_message',
                'text_data': text_data
            }
        )

     # Receive message from room group
    async def chat_message(self, event):
        await self.send(text_data=event['text_data'])