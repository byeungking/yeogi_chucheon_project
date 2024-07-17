from django.urls import path
from . import views

app_name = 'mainApp'

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('chatbot/', views.chatbot_view, name='chatbot_view'),
    path('destinations/', views.destinations, name='destinations'),
]
