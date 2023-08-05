# GIT 이란...
> 분산 버전 관리 시스템
-
1.코드의 변경이력을 기록하고 협업을 원활하게 하는 도구

```

```
## GIT의 3가지 영역
 1. working directory
  - 실제 작업 영역
 2. Staging Area
 - 변경된 파일 중 다음 버전에 포함 시킬 파일들을 선택적 추가 or 제외할 수 있는 중간 준비 영역
 3. Repository
 -  버전 이력과 파일들이 영구적으로 저장되는 영역
    모든 버전과 변경 이력이 기록됨

### git초기화
```bash
$ git init
```
### commit
"버전"

변경된 파일들을 저장하는 행위
사진 찍듯이 기록한다 하여  snapshot 이라고도 함

###  상태 확인 명령어
```bash
$ git status
```

### staging area 에 추가
```bash
$ git add {path}<folder_name>/{file name}
```

### Repository 에 저장하기
```bash
$ git commit -m "commit message"
```

## git 기초 설정
```bash
$ git config --global user.email "kyhan1563@naver.com"
$ git config --global user.name "고유한"

$ git config --global --list
```
### 커밋 기록 확인하기
```bash
$ git log
```

### 직전 커밋 수정하기
```bash
$ git commit --amend
#vim  에서 커밋 내용 수정하기
#1. insertㄹㄹ 눌러서 -삽입상태로 ㅁㄴ든다.
#2. 커밋 메시지를 수정한다.
#3. esc를 눌러서 삽입상태 종료한다.
#4 :wq를 입력해서 저장하고 종료한다.
```
### git 설정 초기화
```bash
# vim을 활용해서 설정 제거하기
# vim git 설정 파일 열기
$ vim ~/.gitconfig
#insert 키: 수정 상태 만들기
#--insert-- 인 상태에서 모든 내용 삭제
# esc:수정상태 종료
#:wq

$ code ~/.gitconfig
```
## git remote -v
원격 저장소 주소 확인 인가?
git remote add origin https://github.com/may15th/TIL.git
git push origin master

## 안녕하세요
```bash
mkdir git_study

```
```bash
mv git_stud git_study
```
```bash
code README.md
```

```bash
git init
```
절대로 desk top에서 git init 하지 말 것.
```bash
code main.py
```

```bash
git 
```
```bash
git rm --cached {파일명}
# 스테이징 에이리어 올라간 파일을 삭제한다
```
vim 창에서 esc누른 후 uuuu연타 치면 원래 상태 돌아옴.
git commit만 칠 경우  vim창이 뜬다
git commit -m "메시지" 이렇게 해야 정상적인 commit  완료
```bash
git log --oneline
git에 많이 쌓였을 때 한 줄로 코드 보여주기 위함\

```

```bash
git remote add origin https://github.com/may15th/TIL.git
git remote -v
git push origin master
```
## 원격 저장소에서 git저장 폴더? 등 불러오기
```bash
git clone {git 주소}
```
```bash
git clone은 git이 아무것도 없을 때 사용
git이 일단 있을 때는 최신버전 업데이트 할 때

\
```
### 원격 저장소 git에 등록
```bash

$ git remote all{remote_nickname}  더 있는데 못적음;;;ㅋㅋㅋ


```



## 원격 저장소에 업로드
```bash
$ git push origin master
```

### 원격 저장소에 있는 내용 복제
-최초로 내려 받을 떄
```bash
$ git clone repository_url
```

# git remote -v로 git hub,lab 다 연결되어 있는지 확인
hub     https://github.com/may15th/TIL.git (fetch)
hub     https://github.com/may15th/TIL.git (push)
origin  https://lab.ssafy.com/kyhan1563/til.git (fetch)
origin  https://lab.ssafy.com/kyhan1563/til.git (push) 

이렇게 떠야지 정상

git remote add hub 이런식으로 적기


# 자리 이동 할 때 git hub, lab자격 주는법
그냥 hub이랑 lab에서 파일 하나씩 클론한 다음에
바탕화면에서 bash키고 클론 해서 열면 자격 자동 생성 된다.

내가 알고 싶은 건... git push만 쳤을때 자동 전송되는 저장소가 lab으로 되어 있는데 이를 hub으로 변경 시키는 법... 뭘까?

### git homework 옮겨 받는 법
 강사님이 올려주는 lectures파일 pull한 이후에 무조건
 ws 파일들 hs파일들 복사 붙여넣기 한 이후에 my_lectures or til에
복붙한 이후에 git에 저장한다.
왜냐하면 강사님한테 받은 lectures는 교수님이 올린 git이라서 git remote 계정이 교수님으로 돼있다.
그래서 내거 git으로 연결되 til 파일이나 my_lectures로 하는 것.