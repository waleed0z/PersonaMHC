from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid
import json

# Import your chatbot and conversation model
from .chatbot import MentalHealthChatbot
from .models import Conversation

def get_session_id(request):
    """
    Helper function to get or create an anonymous session ID.
    """
    if 'anonymous_session_id' not in request.session:
        request.session['anonymous_session_id'] = str(uuid.uuid4())
        request.session.save()
    return request.session['anonymous_session_id']

def chatbot_view(request):
    """
    Render the chat UI and retrieve conversation history.
    """
    # Get the session ID to retrieve the correct conversations
    session_id = get_session_id(request)

    # Fetch conversation history based on user status
    if request.user.is_authenticated:
        conversations = Conversation.objects.filter(user=request.user).order_by('timestamp')
    else:
        conversations = Conversation.objects.filter(anonymous_session_id=session_id).order_by('timestamp')

    return render(request, "chatbot.html", {'conversations': conversations})

@csrf_exempt
def chatbot_response(request):
    """
    Handle AJAX POST request, save to database, and return bot response.
    """
    if request.method == "POST":
        try:
            # We'll assume the client is sending JSON data, which is standard for APIs.
            data = json.loads(request.body)
            user_message = data.get("message", "")
        except json.JSONDecodeError:
            # Fallback for simple form data if not sending JSON
            user_message = request.POST.get("message", "")

        if not user_message:
            return JsonResponse({"reply": "Please enter a message."})
        
        # Determine the user and session ID
        user = request.user if request.user.is_authenticated else None
        session_id = get_session_id(request)

        # Get the bot's response
        chatbot_instance = MentalHealthChatbot(session_id=session_id)

        bot_reply = chatbot_instance.mh_respond(user_message)
        
        # Save the conversation to the database
        Conversation.objects.create(
            user_input=user_message,
            bot_response=bot_reply,
            user=user,
            anonymous_session_id=session_id
        )

        return JsonResponse({"reply": bot_reply})
        
    return JsonResponse({"error": "Invalid request method."})