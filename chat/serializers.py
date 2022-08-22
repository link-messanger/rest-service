from rest_framework import serializers

from chat.models import ChatRoom


class ChatRoomSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()

    def get_messages(self, obj):
        return obj.message.all()

    def get_members(self, obj):
        return obj.member.all()

    class Meta:
        model = ChatRoom
        fields = ['name', 'messages', 'members']
