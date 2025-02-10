from django.shortcuts import render
from django.http import JsonResponse
from .chatbot import MentalHealthChatbot  # Ensure your chatbot is properly imported

# Create a chatbot instance
chatbot_instance = MentalHealthChatbot()

def chatbot_view(request):
    """Render the chat UI."""
    return render(request, "chatbot.html")

def chatbot_response(request):
    """Handle AJAX POST request and return bot response."""
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        if user_message:
            bot_reply = chatbot_instance.mh_respond(user_message)
            return JsonResponse({"reply": bot_reply})
        return JsonResponse({"reply": "Please enter a message."})
    return JsonResponse({"error": "Invalid request method."})
