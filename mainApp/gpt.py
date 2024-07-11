import openai
from dotenv import load_dotenv, find_dotenv
import os

# .env 파일을 추가하고 챗봇의 api를 넣어주세요.
# Please add the .env file and add the api of the chatbot.

# .env 파일의 경로를 찾고 UTF-8로 로드
env_path = find_dotenv()

if env_path:
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
                {"role": "system", "content": "너는 여행 전문 chat GPT야. "
                                              "너를 소개할 때는 여행의 전문가라고 소개해야해"},
                {"role": "system", "content": "사용자가 지역을 말하지 않으면 알아서 해당 주제에 맞는 여행지를 추천해주면 돼."},
                {"role": "system", "content": "사용자가 해외여행을 가고싶은게 아니라면 korea를 기준으로 여행지를 추천해줘"},
                {"role": "system", "content": "여행지를 추천해 줄때 최소한 3가지는 추천해줘."},
                {"role": "system", "content": "여행지에 사이트가 있다면 사이트도 링크로 넣어줘."},
                {"role": "user", "content": question}
            ]
        )
        return response['choices'][0]['message']['content']
else:
    print(".env 파일이 없습니다. 해당 기능을 사용할 수 없습니다.")

    def chatbot():
        print("현재 이 기능을 사용할 수 없습니다. 관리자에게 문의하세요.")
        return None

    def chatbot_response(question):
        print("현재 이 기능을 사용할 수 없습니다. 관리자에게 문의하세요.")
        return "현재 이 기능을 사용할 수 없습니다. 관리자에게 문의하세요."


