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


    def create_img(prompt):

        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="256x256"
            )
            image_url = response['data'][0]['url']
            return image_url
        except openai.error.AuthenticationError:
            return "Incorrect API key provided. Please check your API key and try again."
        except openai.error.InvalidRequestError as e:
            return f"Invalid request: {e}"
        except openai.error.RateLimitError:
            return "Rate limit exceeded. Please wait and try again later."
        except openai.error.OpenAIError as e:
            return f"An error occurred: {e}"


else:
    print(".env 파일이 없습니다. 해당 기능을 사용할 수 없습니다.")

    def create_img():
        print("현재 이 기능을 사용할 수 없습니다. 관리자에게 문의하세요.")
        return None
