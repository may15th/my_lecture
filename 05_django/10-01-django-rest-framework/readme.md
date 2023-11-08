rest api는 json 타입으로 응답하는 것을 권장
페이지만을 응답하는 서버 -> render함수의 역할.

이제는 json 데이터 응답하는 rest api서버로의 변환

json은
키: 밸류 형태로 되어있음.
이 json을 front-end framework들이 페이지로 보내주는 것.

get, post, delete, 

api는
template이 없음
url, view작성하면 끝

template안쓰기 때문에 url굳이 이름 쓰지 않는 것.

어떤 클래스/메서드에는 특정인자를 넣어줘야 하고, 어떤 클래스(Meta)는 괄호를 붙여주지 조차 않고
어떤 클래스는 괄홀를 붙이지만 빈칸으로 둔다.
이건 그 각각 클래스/메서드들의 정의, 약속 같은 것이기 때문에 문맥을 단서삼아 외우는 수 밖에 없다.

ArticleListSerializer(articles, many = True)
many의 default값은 False인데 이렇게 전체 데이터를 불러올 떄는 true설정해주는 것.

drf규칙중에 데코레이터 안붙여주면 assertion error띄우게 되있음. 무조건 데코레이터 씌울 것. GET,POST, PUT,DELETE중 하나 정하기.

api_view 데코레이터로 GET입력했는데
POST 하는 경우 405 오류 뜬다..

POST 생성, PUT 수정, DELETE 삭제

201 created 응답
데이터 생성이 성공했음을 응답하는 것.

실패했을 경우 
400bad request라는 응답 

postman 사용법은 runserver하고 url 그대로 옮겨서 확인하는 것.
그것뿐.

postman POST할 경우 POST창에서
기본은 Params Authorization ... 중\
Body, form-data선택
키-밸류 형태
타이틀, content 만 넣어주면 됨
key title, contetn 넣어주고, values는 쓰고 싶은 제목, 내용 적기

create = post
read = get
update = put
delete = delete

import requests
from pprint import pprint

#json을 python 타입으로 변환
response = requests.get(http://xxxxxx)

pprint(result[0].get('title'))
