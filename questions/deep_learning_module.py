import os
import django
from django.db import models
from django.conf import settings

from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

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
        # 해당 Question과 연결된 모든 Choice 객체의 텍스트와 ID를 가져와서 리스트로 저장
        choices_info = [(choice.choice_text, choice.id) for choice in question.choice_set.all()]

        # 딕셔너리에 추가
        question_choices_dict[question.question_text] = choices_info

    return question_choices_dict


def train_recommendation_model():
    # 데이터 준비
    # 실제 데이터로 교체 필요
    questions = ['여행의 목적을 알려주세요.', '여행 기간을 정해볼까요?']
    choices = ['해변으로 가고 싶어요', '1-3일']

    # 데이터 처리
    encoder = LabelEncoder()
    X = encoder.fit_transform(questions + choices).reshape(-1, 1)
    y = np.array([0, 1])  # 예시 레이블, 실제 레이블로 교체 필요

    # 모델 구성
    model = Sequential()
    model.add(Dense(64, input_dim=1, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(len(set(y)), activation='softmax'))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # 모델 학습
    model.fit(X, y, epochs=10, batch_size=32)

    return model, encoder


# 예측 함수
def predict_destination(question_texts, choice_ids):
    model, encoder = train_recommendation_model()
    inputs = [f"{question}_{choice_id}" for question, choice_id in zip(question_texts, choice_ids)]
    X_input = encoder.transform(inputs).reshape(-1, 1)
    prediction = model.predict(X_input)
    predicted_destination = np.argmax(prediction, axis=1)

    # 실제 예측 결과로 매핑 필요
    destination_mapping = {0: '해변', 1: '산'}
    recommended_destinations = [destination_mapping.get(pred, "추천 결과를 가져오는 데 문제가 발생했습니다.") for pred in
                                predicted_destination]

    return recommended_destinations[0]  # 여러 결과 중 첫 번째 결과 반환


if __name__ == "__main__":
    value = get_question_choices_dict()
    print(value)
