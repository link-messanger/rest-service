from rest_framework import serializers

from chat.models import ChatRoom


class ChatRoomSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    def get_messages(self, obj):
        return obj.messages.all()

    class Meta:
        model = ChatRoom
        fields = ['name', 'messages']
