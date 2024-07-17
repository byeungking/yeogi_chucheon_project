from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.http import JsonResponse
from .api_openai_GPT import chatbot_response

from .models import Banner

# Create your views here.
def main_home(request):
    banners = Banner.objects.all()
    # 기존 컨텍스트와 함께 banners를 추가합니다.
    context = {'banners': banners}
    return render(request, 'mainApp/main_home.html', context)

def destinations(request):
    return render(request, 'mainApp/destinations.html')

@login_required(login_url='common:login')
def chatbot_view(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        response = chatbot_response(question)
        return JsonResponse({'response': response})
    return render(request, 'mainApp/chat.html')
