# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from telegrambot.serializers import UpdateSerializer
from rest_framework import status
from .tasks import bot_update
import logging

logger = logging.getLogger('telegrambot')

class WebhookView(APIView):
    def post(self, request, token):
        logger.info(request.data)
        bot_update.delay(data=request.data)
        serializer = UpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
