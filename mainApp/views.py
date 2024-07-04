from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic
from django.http import JsonResponse
from .gpt import chatbot_response

# Create your views here.
def main_home(request):
    return render(request, 'mainApp/main_home.html')

def destinations(request):
    return render(request, 'mainApp/destinations.html')

def chatbot_view(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        response = chatbot_response(question)
        return JsonResponse({'response': response})
    return render(request, 'mainApp/chat.html')
