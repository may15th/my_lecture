# 관통PJT

관통 프로젝트 명세서 및 예제 코드 저장소입니다.

- 아래 명령어를 이용하여 저장소를 로컬 PC 로 복사하여 활용합니다.
  - 혹은 zip 파일을 다운로드 받아도 괜찮습니다.

```
$ git clone https://lab.ssafy.com/s10/python/pjt.git
```
1. API server의 특징 = 화면 template이 없어졌다.
json형태로 데이터 돌려주는 서버 만들어줄 것.

2. REST = 규칙 사용자의 요청을 ~~식으로 하라고 정해준 것.
 1) url식별자만 표시하자
      create 이런것 쓰지 말자.
 2) HTTP 메소드로 CREATE 같은 것들 표기하자.

3. GET /articled/<int:pk>

데이터 수집 -> db저장 -> 반환하는 api


## 231027
1. 오류 response = requests.get(url).json
이라고만 해서 오류 뜸 .josn()인데... 옆에 소괄호는 왜 항상 붙이는 거냐...

2. api_key를 내 pc에만 저장, github엔 안올릴래 = 환경변수
프로젝트의 환경변수

3. .env파일 API_KEY는 django 환경설정 문제로 작은따옴표나 띄어쓰기 안되고 무조건 붙여쓰기, 큰따옴표로 설정 엄격한 규칙 적용
API_KEY = '123456789' (X)
API_KEY="123456789" (o) 이런식으로.
그리고 .env 파일은 무조건 manage.py랑 같은 위치에 있어야 함.

()의 의미는 상속받겠다.
