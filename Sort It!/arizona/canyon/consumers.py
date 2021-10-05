import asyncio
import json
from django.contrib.auth import get_user_model
# from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
# from .models import Thread, ChatMessage
import time
from time import sleep
import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from .newfile import create_square
from django.shortcuts import render
from django.shortcuts import redirect


class CanyonConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self, event):
        print('connected', event)
        await self.accept()

    async def websocket_receive(self, event):
        print('receive', event)
        front_text = event.get('text', None)
        loaded_dict_data = json.loads(front_text)
        msg = loaded_dict_data.get("message")
        print(msg)
        await create_square(msg)

    async def websocket_disconnect(self, event):
        print('disconnect', event)


class ResultConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self, event):
        print('connected', event)
        await self.accept()
        print('Results Consumer connected')
        def conv(unformatted_message):
            a = {
                "type": "websocket.send",
                "text": unformatted_message,
                "name": 'bhoshaga'
            }
            deets = json.dumps(a)
            return deets

        await self.send(conv('make-button'))

    async def websocket_receive(self, event):
        print('receive', event)
        front_text = event.get('text', None)
        loaded_dict_data = json.loads(front_text)
        msg = loaded_dict_data.get("message")
        print(msg)
        await create_square(msg)

    async def websocket_disconnect(self, event):
        print('disconnect', event)
