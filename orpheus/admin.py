# your_app_name/admin.py

from django.contrib import admin
from .models import Conversation

# Register your model with the admin site
admin.site.register(Conversation)