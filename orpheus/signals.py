from django.dispatch import receiver
from allauth.account.signals import user_logged_in
from django.db import transaction

from .models import Conversation

@receiver(user_logged_in)
def link_anonymous_conversations(sender, request, user, **kwargs):
    with transaction.atomic():
        print(f"User '{user.username}' just signed up. Checking for anonymous chat history.")

        anonymous_session_id = request.session.get('anonymous_session_id')
        
        if anonymous_session_id:
            print(f"Anonymous session ID found in session: {anonymous_session_id}")

            # This is the test line to check if the query is finding anything
            anonymous_conversations = Conversation.objects.filter(anonymous_session_id=anonymous_session_id)
            print(f"Query found {anonymous_conversations.count()} conversation(s) to link.")
            
            if anonymous_conversations.exists():
                anonymous_conversations.update(user=user, anonymous_session_id=None)
                print("Successfully linked conversations and cleared anonymous ID.")
            
            # Clean up the session variable
            del request.session['anonymous_session_id']
            request.session.save()
        else:
            print("No anonymous session ID found in the session. No linking needed.")
