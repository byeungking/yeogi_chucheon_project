import openai
from dotenv import load_dotenv, find_dotenv
import os

# .env 파일의 경로를 찾고 UTF-8로 로드
env_path = find_dotenv()
with open(env_path, 'r', encoding='utf-8') as f:
    load_dotenv(stream=f)

# 환경 변수에서 OpenAI API 키 가져오기
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
    question = input("질문을 입력해주세요: ")

    # ChatGPT 모델에 요청 보내기
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}

        ]
    )
    return response['choices'][0]['message']['content']



def chatbot_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']
