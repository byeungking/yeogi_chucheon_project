import os
import django
from django.conf import settings

# Django 환경 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# 이제 모델 및 뷰를 임포트하고 사용할 수 있습니다.
from questions.models import Question, Choice

def get_question_choices_dict():
    # 빈 딕셔너리 생성
    question_choices_dict = {}

    # 모든 Question 객체에 대해 반복
    for question in Question.objects.all():
        # 해당 Question과 연결된 모든 Choice 객체의 ID를 리스트로 가져옴
        choice_ids = list(question.choice_set.values_list('id', flat=True))
        # 딕셔너리에 추가
        question_choices_dict[question.question_text] = choice_ids

    return question_choices_dict



if __name__ == "__main__":
    value = get_question_choices_dict()
    print(value)
