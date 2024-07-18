# yeogi_chucheon_project


## 프로젝트 설명 (Project Information)
### 이 프로젝트는 여행 추천 사이트입니다. <br>사용자는 "추천 받기" 버튼을 누르고 간단한 질문에 답을 하면, 질문에 맞춰 여행지를 추천받을 수 있습니다. <br>또한 추천된 여행지 주변의 숙박시설이나 레스토랑 등도 추천받을 수 있습니다.


## 실행 방법 (How to Execute)
### 0. 이프로젝트는 파이참, 아나콘다 인터프리터를 사용하였습니다.
### 1. 가상환경 설치 (Installing a Virtual Environment)
python -m venv venv 
<br><br>※이미 venv 폴더가 있을 경우 삭제하고 다시 설치해 주세요.※
### 2. 가상환경 활성화 후 (Enabling a Virtual Environment)
venv\Scripts\activate
### 3. 라이브러리 설치 (Installing the Library)
pip install -r requirements.txt
### 4. 마이그레이션 진행 (Migration)
python manage.py makemigrations <br>
python manage.py migrate
### 5. 서버 시작 (Start Server)
python manage.py runserver


## 개발 진행 상황 (Development progress)

1. 2024-07-04: 첫 번째 커밋  
초기 단계로, 메인 페이지, 회원가입, 로그인 기능이 구현되었습니다.  
간단한 챗봇 기능이 추가되었습니다.

2. 2024-07-05: 챗봇 기능 수정 및 업데이트  
여행 추천에 맞춰 챗봇 기능을 최적화하였습니다.  

3. 2024-07-09: tour API 적용  
외부 여행 정보 API를 통합하여 여행지 정보를 제공하는 기능이 추가되었습니다.  
사이트의 배너가 업데이트되었습니다.  

4. 2024-07-10: 여행 주제에 맞는 히든 메시지 추가  
사용자 경험을 향상시키기 위해 여행 주제와 관련된 히든 메시지가 추가되었습니다.  
홈페이지의 비주얼이 업데이트되었습니다.  

5. 2024-07-11: api 토큰이 없어도 실행 가능  
.env 파일이 없어도 프로젝트가 실행 가능 하도록 변경되었습니다.

6. 2024-07-18: 결과페이지에 이미지생성 api추가, 추천 알고리즘 작성중  
결과 페이지에 이미지 생성이 추가되고 추천알고리즘 구현중에 있습니다. 
## Author github : https://github.com/byeungking
