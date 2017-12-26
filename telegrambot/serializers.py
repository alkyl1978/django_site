# -*- coding: utf-8 -*-
from rest_framework import serializers
from telegrambot.models import User, Chat, Message, Update
from datetime import datetime
import time
import logging

logger = logging.getLogger('telegrambot')


class TimestampField(serializers.Field):

    def to_internal_value(self, data):
        return datetime.fromtimestamp(data)
    
    def to_representation(self, value):
        return int(time.mktime(value.timetuple()))


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'username')

class ChatSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Chat
        fields = ('id', 'type', 'username', 'first_name')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    message_id = serializers.IntegerField()
    from_ = UserSerializer(many=False, source="from_user")
    chat = ChatSerializer(many=False)
    date = TimestampField()
    text = serializers.CharField(required=True)
    
    class Meta:
        model = Message
        fields = ('message_id', 'from_', 'date', 'chat', 'text')
        
    def __init__(self, *args, **kwargs):
        super(MessageSerializer, self).__init__(*args, **kwargs)
        self.fields['from'] = self.fields['from_']
        del self.fields['from_']

class UpdateSerializer(serializers.HyperlinkedModelSerializer):
    update_id = serializers.IntegerField()
    message = MessageSerializer(many=False)
    
    class Meta:
        model = Update
        fields = ('update_id', 'message')
    
    def create(self, validated_data):
        logger.info(validated_data)
        update_id = validated_data.get('update_id')
        message=validated_data.get('message')
        logger.info(message)
        return validated_data
        
