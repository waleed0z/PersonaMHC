from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()
class Conversation(models.Model):
    anonymous_session_id = models.UUIDField(default=uuid.uuid4, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    user_input = models.TextField(null=True)
    bot_response = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.user:
            return f"Conversation with {self.user.username} at {self.timestamp}"
        else:
            return f"Anonymous Conversation at {self.timestamp}"