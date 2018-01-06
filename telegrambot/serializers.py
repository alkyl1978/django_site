# -*- coding: utf-8 -*-
from rest_framework import serializers
from telegrambot.models import User, Chat, Message, Update
from datetime import datetime
import time
import logging

logger = logging.getLogger('telegrambot')

class UserSerializer(serializers.ModelSerializer):
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

class ChatSerializer(serializers.ModelSerializer):
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

class MessageSerializer(serializers.ModelSerializer):
    message_id = serializers.IntegerField()
    from_user  = UserSerializer(many=False)
    chat       = ChatSerializer(many=False)
    date       = serializers.IntegerField()
    text       = serializers.CharField(required=True)
    
    class Meta:
        model = Message
        fields = ('message_id', 'from_user', 'date', 'chat', 'text')
        depth = 1

    def to_internal_value(self, data):
        if data.get('from'):
            data['from_user']=data.pop('from')
        return data

    def create(self, validated_data):
        print validated_data
        return Message.objects.create(**validated_data)

class UpdateSerializer(serializers.ModelSerializer):
    update_id = serializers.IntegerField()
    message = MessageSerializer(many=False)
    
    class Meta:
        model = Update
        fields = ('update_id', 'message')
        depth = 1

    def update(self, instance, validated_data):
        print validated_data
        return instance

    def create(self, validated_data):
        mesg = validated_data.pop('message')
        mesg_mod = Message.objects.filter(message_id=mesg.get('message_id'))
        print mesg_mod
        return Update.objects.create(Message=mesg_mod ,**validated_data)