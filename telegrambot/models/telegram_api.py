# -*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __unicode__(self):
        if self.first_name:
            return "%s" % self.first_name
        elif self.username:
            return "%s" % self.username
        else:
            return "%d" % self.id


class Chat(models.Model):

    PRIVATE, GROUP, SUPERGROUP, CHANNEL = 'private', 'group', 'supergroup', 'channel'

    TYPE_CHOICES = (
        (PRIVATE, 'Private'),
        (GROUP, 'Group'),
        (SUPERGROUP, 'Supergroup'),
        (CHANNEL, 'Channel'),
    )

    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

    def __unicode__(self):
        return "%s" % (self.title or self.username)
    
    def is_authenticated(self):
        return hasattr(self, 'auth_token') and not self.auth_token.expired()

class Message(models.Model):

    message_id = models.BigIntegerField( primary_key=True)
    from_user = models.ForeignKey(User, related_name='messages', verbose_name="User")
    date = models.DateTimeField('Date')
    chat = models.ForeignKey(Chat, related_name='messages', verbose_name="Chat")
    forward_from = models.ForeignKey(User, null=True, blank=True, related_name='forwarded_from',
                                     verbose_name="Forward from")
    text = models.TextField(null=True, blank=True, verbose_name="Text")
    

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __unicode__(self):
        return "(%s,%s)" % (self.from_user, self.text or '(no text)')
    
class Update(models.Model):
    
    update_id = models.BigIntegerField('Id', primary_key=True)
    message = models.ForeignKey(Message, null=True, blank=True, verbose_name='Message', 
                                related_name="updates")
    
    class Meta:
        verbose_name = 'Update'
        verbose_name_plural = 'Updates'
    
    def __unicode__(self):
        return "%s" % self.update_id    
