from django.db import models
from django.utils import timezone

class Conversation(models.Model):

    user_input = models.TextField(null=True)
    bot_response = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
