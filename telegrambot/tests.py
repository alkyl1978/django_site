# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from telegrambot.serializers import UpdateSerializer
import json
from telegrambot.models.bot import Bot
from rest_framework.test import APIRequestFactory

class UpdateMessageTest(TestCase):
    factory = APIRequestFactory()
    json_data = {}
    data ={}
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        
    def setUp(self):
        # настройка данных
        print("setUp: Run once")
        b=Bot.objects.create(bot='468735875:AAEwe5Y0HA5GgvIstyC7u5hIkkX9yIftUMg')
        self.json_data=open("test/data.json").read()
        self.data = json.loads(self.json_data)
        b.save()
    def tearDown(self):
        # Очистка после каждого метода
        print("def tearDown(self):")
        pass
    
    def test_update_serializers(self):
         self.assertEqual(Bot.objects.count(),1)
         serializer = UpdateSerializer(data=self.data)
         self.assertTrue(serializer.is_valid())
         serializer.save()
         print("setUp: Run stop")
