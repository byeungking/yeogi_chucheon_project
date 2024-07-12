from dotenv import load_dotenv, find_dotenv
import os
import requests

# .env 파일을 추가하고 챗봇의 api를 넣어주세요.
# Please add the .env file and add the api of the chatbot.

# .env 파일의 경로를 찾고 UTF-8로 로드
env_path = find_dotenv()

if env_path:
    with open(env_path, 'r', encoding='utf-8') as f:
        load_dotenv(stream=f)

    # 글로벌 변수
    api_key = os.getenv("KorService1_API_KEY")
    base_url = 'http://apis.data.go.kr/B551011/KorService1/'

    def tourist_printout():
        operation_code = "areaBasedList1"
        result_url = base_url + operation_code
        params = {
            'ServiceKey': api_key,  # 발급받은 API 키 입력
            'numOfRows': 12,  # 한 페이지 결과 수 (조정 가능)
            'pageNo': 1,  # 페이지 번호
            'MobileOS': 'ETC',  # 모바일 OS
            'MobileApp': 'AppTest',  # 애플리케이션 이름
            'contentTypeId': '25',  # 지역 코드 (예시로 '1' 입력)
            '_type': 'json',  # 응답 포맷 (json)
            'areaCode': 1,
            'sigunguCode': "",
            'cat1': "C01",
            'cat2': "C0115",
            'cat3': "",
        }

        response = requests.get(result_url, params=params)
        response.raise_for_status()

        data = response.json()
        items = data['response']['body']['items']['item']

        return items

else:
    print(".env 파일이 없습니다. 해당 기능을 사용할 수 없습니다.")

    def tourist_printout():
        print("현재 이 기능을 사용할 수 없습니다. 관리자에게 문의하세요.")
        return None
