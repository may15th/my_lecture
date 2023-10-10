DROP TABLE articles;

CREATE TABLE articles(
id INTEGER  PRIMARY KEY AUTOINCREMENT,
title VARCHAR(100) NOT NULL,
content VARCHAR(200) NOT NULL,
createdAt DATE NOT NULL);

INSERT INTO
  articles(title, content, createdAt)
 VALUES
  ('제목', '내용','2000-01-11');


SELECT * FROM articles;

INSERT INTO
  articles(title, content, createdAt)
 VALUES
  ('제목2', '내용2','2000-01-11'),
  ('제목3', '내용3','2000-01-11'),
  ('제목4', '내용4','2000-01-11');
  
-- 함수 위치인자 쓰듯이 값을 다 넣어준 경우에는 column 명 안써줘도 된다.Address

INSERT INTO articles(title, content, createdAt)
VALUES
('제목5', '내용5', '2000-01-11');


--테이블이 가진 모든 데이터 삭제
DELETE FROM articles;

--5번 게시글만 삭제
DELETE FROM articles
 where rowid = 5;

 --1번 게시글만 삭제
DELETE FROM articles
 where rowid = 1;

 INSERT INTO articles
 (rowid, title, content, createdAt)
 VALUES
 (1,'제목1','내용1','2000-01-01');

--1번 게시글의 제목을 '수정된 제목'으로 작성
--UPDATE
UPDATE articles
SET title = '수정된 내용'
WHERE id = 1;

--2번 게시글의 제목을 '2번으로' 2번게시글 내용을 '수정'

UPDATE articles
SET Title = '2번으로',
    content = '수정'
WHERE id = 2;

SELECT * FROM articles;

-- articles 테이블에서 작성일이 
-- 오래된 순으로 레코드 2개 삭제

delete from articles
-- where 절 통해서 삭제 대상이 될 record 찾기
--where절에 작성한 내용을 통해 얻어진 데이터들을 삭제
-- id = 1 -> id가 1인 데이터 하나반환
-- 작성일이 오래된 데이터 2개  찾아야...
-- 작성일이 오래된 데이터 2개의 id값을 찾기

WHERE id IN(
SELECT id FROM articles
ORDER BY createdAt LIMIT 2);


SELECT id FROM articles
ORDER BY createdAt LIMIT 2;


