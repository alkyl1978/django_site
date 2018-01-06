# -*- coding: utf-8 -*-
from rest_framework import serializers
from telegrambot.models import User, Chat, Message, Update
import logging

logger = logging.getLogger('telegrambot')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'username','is_bot' , 'language_code')
        


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'type', 'username', 'first_name')


class MessageSerializer(serializers.ModelSerializer):
    from_user  = UserSerializer(many=True)
    chat       = ChatSerializer(many=True)
    
    class Meta:
        model = Message
        fields = ('message_id', 'from_user', 'date', 'chat', 'text')

    def to_internal_value(self, data):
        if data.get('from'):
            data['from_user']=data.pop('from')
        return data


class UpdateSerializer(serializers.ModelSerializer):
    message = MessageSerializer(many=True)
    
    class Meta:
        model = Update
        fields = ('update_id', 'message')
