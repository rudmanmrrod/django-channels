"""
Django Realtime Chat & Notifications
"""
## @package chat.consumers
#
# Consumer del web socket
# @version 1.0
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'chat',
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'chat',
            self.channel_name
        )

    def receive(self, text_data):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            'chat',
            {
                'type': 'chat_message',
                'text_data': text_data
            }
        )

     # Receive message from room group
    def chat_message(self, event):
        self.send(text_data=event['text_data'])