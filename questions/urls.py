from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('<int:question_id>/', views.question_detail, name='question_detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('result/', views.result, name='result'),
    path('recommendation/', views.get_tourist_data, name='recommendation'),
]
