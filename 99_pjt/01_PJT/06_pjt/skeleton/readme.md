extension, ipython 설치 이유 - shellplus사용이 목적. 안 사용할거면 없어도 됨.
부트 스트랩 적용 기본 코드
# django github치면 폴더 따라 가면 궁금한 코드 확인가능.
구글링 + 공식문서 로 문제 해결

migrations.0001_initial.py 에 스키마 생성됨.

설계 -> 엔티티, 스키마
구현 -> 테이블

엔티티 - 무엇을 만들까? 작성된 것.
        ex_회원은 user_name, password가 있다.
        기본적으로 뭘 만들지 작성한 것.

스키마 - 엔티티에서 나아가서 제약조건이나 자세한 것들
        어떻게 만들까? user_name = 문자열, unique, pqssword : not NULL, 8자 이상 등.

테이블 - 스키마를 토대로 생성한 것.

사실 현장에선 섞어 쓴다고 함...



django = 세션으로 유저 관리함을 기본으로 함.
로그인
1. 세션데이터 생성
2. db에 저장
3. 세션 id를 클라이언트에 줄 수 있게 쿠키에 저장




# 오류 해결 과정
1. template does not exist at accounts/login 오류
떠서 urls.py 다 확인했는데, accounts/login 잘돼 있어서 왜 안됐나 싶었다.
그 이유를 살펴보니, template파일 넣어놓는 templates/accounts여야 하는데
폴더명을 acoounts로 해놓은 것...
성은이한테 리뷰 받아서 해결...

-> template does not exist오류 뜰 경우 urls.py 등 파일 경로 명만 확인 할게 아니라
실제 폴더명도 꼭 확인할 것. 한 글자 한 글자 읽어봐야 함.

2. 로그아웃 버튼을 눌러도 로그아웃이 안뜨는 오류.
주헌이한테 코드 리뷰 부탁 
확인해보니, accounts폴더의 urls.py, views.py 등 모두 오류가 없어보였다.
보통 이런대서 오류가 생기면 오류메시지가 뜬는데, 오류메시지가 안떴다.
2가지로 미루어봤을 때 로그아웃 버튼 클릭이 로그아웃 url을 못 불러온다는 추측을 했다.
즉, navbar.html에 이상이 있을 것이라 생각.
주헌이가 </form>이 로그아웃 버튼을 감싸지 못함을 발견했다...
그래도 내 추측이 디버깅 과정에서 일치한건 꽤 잘한 것 같다.

3. 댓글 상세페이지로 이동이 안되는 오류. 
AttributeError at /boards/1/
'Board' object has no attribute 'comments'
오류메시지가 떴고

C:\Users\SSAFY\Desktop\PJT06\skeleton\boards\views.py, line 23, in detail
    comments = board.comments.all() 
오류 뜬 부분은 여기라고 뜨는데

skeleton code에 models.py - 
clas Comment()
    board = models.ForeignKey(Board, on_delete=models.CASCADE, ) 
        마지막 인자 related_name ='comments' 를 빼놨었는데
        이게 원인이었다...
        왜 그런지는 인강들으면서 정리해야겠다.

이 오류 같은 경우엔 Board가 있는 models에도 이상이 없었고, 
쟝고가 오류 위치라고 명시해준 comments = board.comments.all()도 이상이 없는 코드였다.
오류메시지를 맹신하면 안되고 깊은 이해가 필요하다.


## 231020 todo 
댓글 기능 이후 구현 필요


## 231025 오류
OperationalError at /boards/
no such table: boards_board
뜬 이유 자리 바꾸면서 migration을 안했기 때문에 
boards라는 테이블이 없다고 표시해준 것.

