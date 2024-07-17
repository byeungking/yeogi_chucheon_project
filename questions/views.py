from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

# 모델
from .models import Question, Choice
from .api_tour import tourist_printout
from .api_openai_dalle import create_img

# 외부 라이브러리
import requests

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question_count = Question.objects.count()
    return render(request, 'questions/question_detail.html', {'question': question, 'question_count': question_count})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'questions/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if 'selected_choices' not in request.session:
            request.session['selected_choices'] = {}

        selected_choices = request.session['selected_choices']
        selected_choices[question_id] = selected_choice.id
        request.session['selected_choices'] = selected_choices

        # Find the next valid question ID
        question_count = 0
        next_question_id = question_id + 1
        total_questions = Question.objects.count()

        while question_count <= total_questions:
            if Question.objects.filter(pk=next_question_id).exists():
                return redirect('questions:question_detail', question_id=next_question_id)
            next_question_id += 1
            question_count += 1

        # If all questions are answered, go to result page
        return redirect('questions:result')


def result(request):
    selected_choices = request.session.get('selected_choices', {})
    selected_choices_list = []

    for question_id, choice_id in selected_choices.items():
        question = get_object_or_404(Question, pk=question_id)
        choice = question.choice_set.get(pk=choice_id)
        selected_choices_list.append((question, choice))

    return render(request, 'questions/result.html', {'selected_choices': selected_choices_list})

def get_tourist_data(request):
    prompt = "Random Place"
    items = tourist_printout()
    ai_image = create_img(prompt)
    context = {'items': items, 'ai_image':ai_image}
    try:

        return render(request, 'questions/recommendation.html', context)

    except requests.exceptions.RequestException as e:

        return render(request, 'questions/recommendation.html', {'message': str(e)})
