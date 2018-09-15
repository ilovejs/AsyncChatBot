import json, re
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.checks import Error

class ChatConsumer(AsyncWebsocketConsumer):
    def init(self):
        self.dob = ''
        self.gendar = ''
        self.age = 0
        self.name = ''
        self.dob_regx = re.compile(r'\d{2}-\d{2}-\d{4}')
        self.smoker = ''

    async def wrap_msg(self, msg):
        self.init()
        # Send message to room
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': msg
        }))

    async def connect(self):
        await self.accept()
        await self.wrap_msg("Hello, I am going to ask you few questions that will help me know you better?")
        await self.wrap_msg("What is your name?")

    async def disconnect(self, close_code):
        print('discounted')

    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        msg = text_data_json['message'].replace('\n','').strip()

        if msg in ['Male','Female']:
            self.gendar = msg
            msg = 'When were you born?'
        elif self.dob_regx.match(msg):
            self.dob = msg
            msg = 'Are you a smoker?'
        elif msg in ['Yes','No']:
            self.smoker = msg
            msg = 'Thank you. Press "Done" for results.'
        else:
            print('get name')
            self.name = msg
            msg = 'Are you male or female?'

        self.wrap_msg(msg)

    async def chat_message(self, event):
        message = event['message']
        print('Not Implemented ..........')
        # raise Error('Not Implemented')

        # Send message to WebSocket
        # await self.send(text_data=json.dumps({
        #     'message': message
        # }))
