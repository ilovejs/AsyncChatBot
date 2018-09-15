# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
# from string import strip

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')
        await self.accept()

    async def disconnect(self, close_code):
        print('discounted')

    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message'].replace('\n','').strip()

        if message in ['Male','Female']:
            message = 'When were you born?'
        elif message == '03-26-1989':        # Let user input date in (dd-mm-yyyy) format
            message = 'Are you a smoker?'
        else: # Yes or No
            message = 'Thank you. Press "Done" for results.'

        # Send message to room group
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message
        }))

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        # await self.send(text_data=json.dumps({
        #     'message': message
        # }))
