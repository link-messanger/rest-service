from rest_framework.generics import RetrieveAPIView, ListAPIView

from chat.models import ChatRoom
from chat.serializers import ChatRoomSerializer


class ChatRoomView(RetrieveAPIView):

    def get_queryset(self):
        name = self.kwargs['name']
        return ChatRoom.objects.filter(name=name)

    serializer_class = ChatRoomSerializer
    lookup_field = 'name'
