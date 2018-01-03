# -*- coding: utf-8 -*-
from rest_framework import serializers
from telegrambot.models import User, Chat, Message, Update
from datetime import datetime
import time
import logging

logger = logging.getLogger('telegrambot')


class TimestampField(serializers.Field):

    def to_internal_value(self, data):
        print 'def to_internal_value data = {}' .format(data)
        try:
             return datetime.fromtimestamp(data)
        except TypeError:
             return data

    def to_representation(self, value):
        print 'def to_representation value = {}'.format(value)
        return int(time.mktime(value.timetuple()))


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'username','is_bot' , 'language_code')
        
    def create(self, validated_data):
        mod = self.Meta.model.objects.filter(id=validated_data.get('id'))
        if not mod:
            mod=mod.create(**validated_data)
            mod.save()
        return mod

class ChatSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Chat
        fields = ('id', 'type', 'username', 'first_name')

    def create(self, validated_data):
        mod = self.Meta.model.objects.filter(id=validated_data.get('id'))
        if not mod:
            mod=mod.create(**validated_data)
            mod.save()
        return mod

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

    def create(self, validated_data):
        mod = self.Meta.model.objects.filter(message_id=validated_data.get('message_id'))
        if not mod:
            mod=mod.create(**validated_data)
            mod.save()
        return mod
    
class UpdateSerializer(serializers.HyperlinkedModelSerializer):
    update_id = serializers.IntegerField()
    message = MessageSerializer(many=False)
    
    class Meta:
        model = Update
        fields = ('update_id', 'message')
        
    def create(self, validated_data):
        user_bot = validated_data.get('message').get('from_user')
        chat_bot = validated_data.get('message').get('chat')
        mesg_bot = validated_data.get('message')
        update_bot = validated_data.get('update_id')
        user_ser = UserSerializer(data=user_bot)
        if user_ser.is_valid():
             user_ser.save()
        chat_ser = ChatSerializer(data=chat_bot)
        if chat_ser.is_valid():
             chat_ser.save()
        dat = mesg_bot.pop('date')
        mesg_bot.append('date',)
        mesg_ser = MessageSerializer(data=mesg_bot)
        if mesg_ser.is_valid():
            mesg_mod = mesg_ser.save()
        mod = self.Meta.model.objects.filter(update_id=validated_data.get('update_id'))
        if not mod:
            mod=mod.create(update_id=update_bot,message=mesg_mod)
            mod.save()
        return mod
    
