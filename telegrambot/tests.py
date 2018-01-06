# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from telegrambot.serializers import UpdateSerializer
import json
from telegrambot.models.bot import Bot
from rest_framework.test import APIRequestFactory
from telegrambot.models import User, Chat, Message, Update

class UpdateMessageTest(TestCase):
    factory = APIRequestFactory()
    json_data = {}
    data ={}
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        # настройка данных
        b=Bot.objects.create(bot='468735875:AAEwe5Y0HA5GgvIstyC7u5hIkkX9yIftUMg')
        self.json_data=open("test/data.json").read()
        self.data = json.loads(self.json_data)
        b.save()
    def tearDown(self):
        # Очистка после каждого метода
        pass

    def test_update_serializers(self):
         self.assertEqual(Bot.objects.count(),1)
         serializer = UpdateSerializer(data=self.data)
         print serializer
         self.assertTrue(serializer.is_valid())

         serializer.save()
         self.assertEqual(User.objects.count(),1)
         self.assertEqual(Chat.objects.count(),1)