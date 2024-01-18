from django.shortcuts import render
from .chatbot import MentalHealthChatbot

chatbot = MentalHealthChatbot()

def chatbot_view(request):
    chat_history = []
    if request.method == 'POST':
        user_input = request.POST['user_input']
        response = chatbot.mh_respond(user_input)
        chat_history.append((user_input, response))
    return render(request, 'chatbot.html', {'chat_history': chat_history})