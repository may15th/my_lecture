CREATE TABLE examples(

LastName VARCHAR(50) NOT NULL,
firstName VARCHAR(50) NOT NULL
);

-- 테이블 만들때 id지정 안하면 기본으로 아무거나 지정된다.

PRAGMA table_info('examples');

-- NOT NULL : NULL값을 허용하지 않도록 지정
-- FOREIGN KEY : 다른 테이블과 외래 키 관게의 정의
-- RDBMS에서 


-- 데이터 디폴트값 넣어줘야 됨.

ALTER TABLE
 examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL
DEFAULT
 '부산';


ALTER TABLE
 examples
ADD COLUMN
  AGE INTEGER NOT NULL
  DEFAULT
  1;


ALTER TABLE
 examples
ADD COLUMN
  Address INTEGER NOT NULL
  DEFAULT
  1

-- 컬럼 명 수정

ALTER TABLE
 examples
 RENAME COLUMN
 Address to PostCode;


-- 컬럼명 삭제
ALTER TABLE
 examples
DROP COLUMN
 PostCode;

-- 테이블명 삭제

ALTER TABLE
 new_examples
RENAME TO
 examples;

-- 테이블 삭제
DROP TABLE examples;