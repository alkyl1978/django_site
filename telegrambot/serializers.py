# -*- coding: utf-8 -*-
from rest_framework import serializers
from telegrambot.models import User, Chat, Message, Update
from datetime import datetime
import time
import logging

logger = logging.getLogger('telegrambot')

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
    from_user  = UserSerializer(many=False)
    chat       = ChatSerializer(many=False)
    date       = serializers.IntegerField()
    text       = serializers.CharField(required=True)
    
    class Meta:
        model = Message
        fields = ('message_id', 'from_user', 'date', 'chat', 'text')

    def to_internal_value(self, data):
        if data.get('from'):
            data['from_user']=data.pop('from')
        return data

    def create(self, validated_data):
        data_user = validated_data.pop('from_user').get('id')
        data_chat = validated_data.pop('chat').get('id')
        message_id = validated_data.get('message_id')
        mod_mesg = self.Meta.model.objects.filter(message_id=message_id)
        if not mod_mesg:
            mod_mesg=mod_mesg.create(from_user=data_user,chat=data_chat,**validated_data)
            mod_mesg.save()
        return mod_mesg
    
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
        update_bot = validated_data.pop('update_id')
        user_ser = UserSerializer(data=user_bot)
        if user_ser.is_valid():
             user_ser.save()
             print 'USER is_valid'
        chat_ser = ChatSerializer(data=chat_bot)
        if chat_ser.is_valid():
             chat_ser.save()
             print 'CHAT is_valid'
        mesg_ser = MessageSerializer(data=mesg_bot)
        if mesg_ser.is_valid():
            print 'MESSAGE is_valid'
            mesg_ser.save()
        mod = self.Meta.model.objects.filter(update_id=update_bot)
        #if not mod:
        #    mod.create(update_id=update_bot,**validated_data)
        #    mod.save()
        return mod
    
