import json
import re
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dob = ''
        self.gender = ''
        self.state = 0  # state machine
        self.age = 0
        self.name = ''
        self.dob_regex = re.compile(r'\d{2}-\d{2}-\d{4}')
        self.smoker = False

    async def wrap_msg(self, msg):
        # Send message to room
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': msg
        }))

    async def connect(self):
        await self.accept()
        await self.wrap_msg("Hello, I am going to ask you few questions that will help me know you better?")
        # await self.wrap_msg("What is your name?")

    async def disconnect(self, close_code):
        print('discounted')

    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        text_data_json = json.loads(text_data)
        # case-insensitive
        msg = text_data_json['message'].replace('\n', '').strip().lower()

        if msg in ['male', 'female']:
            self.state = 2
            self.gender = msg
            msg = r'When were you born?  format:dd-mm-yyyy'
        elif self.dob_regex.match(msg):
            self.dob = msg
            msg = r'Are you a smoker?'
        elif msg in ['yes', 'no']:
            self.smoker = True
            msg = r'Thank you. Press <form method="get" action="/chat/done3">'\
                  r'<button type="submit">Continue</button></form> for results.'
        elif self.state == 0:
            self.state = 1
            self.name = msg
            msg = r'Are you male or female?'
        else:
            msg = r"Sorry. I don't understand."

        await self.wrap_msg(msg)

    async def done(self):
        fmsg = r'{} was born in {} and is a {} {}.'.format(
            self.name, self.dob, self.gender,
            'smoker' if self.smoker else 'non-smoker'
        )
        await self.wrap_msg(fmsg)
