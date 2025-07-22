from django.db import models
from django.utils import timezone

class Post(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
