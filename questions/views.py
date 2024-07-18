from django.shortcuts import render, redirect

# 모델
from .models import Question, Choice
from .api_tour import tourist_printout
from .api_openai_dalle import create_img
# 외부 라이브러리
import requests


def question_detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return render(request, 'questions/error.html', {'error_message': "Question not found."})

    question_count = Question.objects.count()
    return render(request, 'questions/question_detail.html', {'question': question, 'question_count': question_count})


def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return render(request, 'questions/error.html', {'error_message': "Question not found."})

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
        next_question_id = question_id + 1
        question_count = 1
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

    if not selected_choices:
        # 세션에 선택된 데이터가 없으면 에러 메시지 추가
        return render(request, 'questions/result.html', {'error_message': "No choices have been made."})

    for question_id, choice_id in selected_choices.items():
        try:
            question = Question.objects.get(pk=question_id)
            choice = question.choice_set.get(pk=choice_id)
            selected_choices_list.append((question, choice))
        except (Question.DoesNotExist, Choice.DoesNotExist):
            continue  # 해당 질문 또는 선택지가 없는 경우 무시

    if not selected_choices_list:
        return render(request, 'questions/error.html', {'error_message': "No valid choices found."})

    return render(request, 'questions/result.html', {'selected_choices': selected_choices_list})


def get_tourist_data(request):
    prompt = "A fantasy ruins"
    items = tourist_printout()
    ai_image = create_img(prompt)
    context = {'items': items, 'ai_image': ai_image}
    try:

        return render(request, 'questions/recommendation.html', context)

    except requests.exceptions.RequestException as e:

        return render(request, 'questions/recommendation.html', {'message': str(e)})





def my_view(request):
    # 함수 호출하여 딕셔너리 가져오기
    question_choices_dict = get_question_choices_dict()

    # 템플릿에 딕셔너리 전달
    return render(request, 'my_template.html', {'question_choices_dict': question_choices_dict})

