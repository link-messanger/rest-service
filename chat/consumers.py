import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from chat.models import ChatRoom, Member, Message


class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.user = None
        self.message = None

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['name']
        self.user = self.scope['user']
        member = Member.objects.get(user=self.user)

        chat_room = ChatRoom.objects.get(name=self.room_name)
        chat_room.member.add(member)

        self.accept()

    def disconnect(self, close_code):
        member = Member.objects.get(user=self.user)
        chat_room = ChatRoom.objects.get(name=self.room_name)
        chat_room.member.remove(member)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.message = text_data_json['message']

        chat_room = ChatRoom.objects.get(name=self.room_name)
        member = Member.objects.get(user=self.user)

        Message.objects.create(user=member, chat_room=chat_room, content=self.message)
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type': 'chat_message',
                'message': self.message
            }
        )
