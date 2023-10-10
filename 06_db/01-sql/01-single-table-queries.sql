-- 01. Querying data
--(하이픈 두개가 sql문에서는 주석)
SELECT
    LastName
FROM
    employees;



SELECT
    LastName,FirstName
FROM
    employees;



SELECT
    *
FROM
    employees;
-- * asterisk가 거의 모든 언어에서 all을 뜻함.



SELECT
    FirstName AS '이름'
FROM
    employees;
--실제로 db가 바뀐 건 아니 출력할 때만 바뀐것.

SELECT
    Name, Milliseconds / 60000 AS '재생시간(분)'
FROM
    tracks;

-- '/' 하나뿐인데도 소수점 사라진 거 파이썬이랑 다르다 꼭 기억!!!

-- SELECT 문을 사용하여  ㅌ이블 데이터를 조회 및 반환


-- 02. Sorting data

--order by 1

SELECT
    FirstName
FROM
    employees
ORDER BY
    FirstName;

--order by2

SELECT
    FirstName
FROM
    employees
ORDER BY
    FirstName DESC;

--order by 3

SELECT
    Country,City
FROM
    customers
ORDER BY
    Country DESC,
    City ASC;


-- ORDER BY 4 
SELECT
    Name, Milliseconds /60000 AS '재생시간(분)'
FROM
    tracks
ORDER BY
    Milliseconds DESC;



-- NULL 정렬 예시

SELECT
 ReportsTo
FROM
 employees
 ORDER BY
  ReportsTo;



-- 03. Filtering data

SELECT DISTINCT
    Country
FROM
    customers
ORDER BY
    Country;



-- 04. Grouping data

--WHERE1
SELECT
    LastName, FirstName, City
FROM
    customers
WHERE
    City = 'Prague';

--WHERE2
SELECT
    LastName, FirstName, City
FROM
    customers
WHERE
    City != 'Prague';

--WHERE3
SELECT
    LastName, FirstName, Company, Country
FROM
    customers
WHERE
    Company IS NULL AND Country = 'USA';


--WHERE4
SELECT
    LastName, FirstName, Company, Country
FROM
    customers
WHERE
    Company IS NULL OR Country = 'USA';

-- 값이 NULL일 떄는 '='붙여주는 게 아니라 IS 써줌 NULL은 VALUE값이 아니라 DATA TYPE이기 때문.



--where5
SELECT
 Name, Bytes
FROM
 tracks
WHERE
 100000 <= Bytes <= 500000;

-- 위 SQL문 틀렸음 SQL문에서는 WHERE절로 조건 줄 때 BETWEEN구문 사용함.

SELECT
 Name, Bytes
FROM
 tracks
WHERE
 Bytes BETWEEN 100000 AND 500000;



-- WHERE6 S-F-W-O  SF WORLD라고 생각 ㅋㅋ
SELECT
 Name, Bytes
FROM
 tracks
WHERE
 Bytes BETWEEN 100000 AND 500000
ORDER BY
 Bytes;

-- where7 반복이 거슬려. or의 반복.
SELECT
 LastName, FirstName, Country
FROM
 customers
WHERE
 Country = 'Canada'
 or Country = 'Germany'
 or Country = 'France';

-- IN 구문 활용
SELECT
 LastName, FirstName, Country
FROM
 customers
WHERE
 Country IN('Canada', 'Germany', 'France');

-- WHERE 8 NOT IN 구문 

SELECT
 LastName, FirstName, Country
FROM
 customers
WHERE
 Country NOT IN('Canada', 'Germany', 'France');

-- WHERE 9 문자의 일부분에 대한 일치값

SELECT
 LastName,FirstName
FROM
 customers
WHERE
 LastName LIKE '%son';

-- LIKE 문자 일부분에 대한 일치값 WILD CARD %, 

-- WHERE 10

SELECT
 LastName,FirstName
FROM
 customers
WHERE
 FirstName LIKE '___a';

-- limit, offset
SELECT
 TrackId, Name, Bytes
FROM
 tracks
ORDER BY
 Bytes DESC
LIMIT 7;

-- offset 1
SELECT
 TrackId, Name, Bytes
FROM
 tracks
ORDER BY
 Bytes DESC
LIMIT 3, 4;

-- offset2 둘 다 사용 가능!
SELECT
 TrackId, Name, Bytes
FROM
 tracks
ORDER BY
 Bytes DESC
LIMIT 4 OFFSET 3;

--group by    -- SF WORLD IS GREATE!로 기억 SELECT- FROM- WHERE- ORDER BY-  
SELECT
 Country, Count(*)
FROM
 customers
Group BY
 Country;

-- DISTINCT보다 강력한 기능 데이터 수 등 출력 가능 각 그룹 집계 된 값 계산 가능!!

-- GROUP BY 활용
SELECT
 Composer, AVG(Bytes)
FROM
 tracks
Group BY
 Composer
ORDER BY
 AVG(Bytes) DESC;

--집계함수에 대한 조건 절은 where가 아닌 having절 사용해야 함!!
SELECT
 Composer, AVG(Milliseconds/60000) AS avgOfMinute
FROM
 tracks
Group BY
Composer
ORDER BY
 avgOfMinute < 10;

--집계함수에 대한 조건 절은 where가 아닌 having절 사용해야 함!!
SELECT
 Composer, AVG(Milliseconds/60000) AS avgOfMinute
FROM
 tracks
Group BY
 avgOfMinute < 10
HAVING
 avgOfMinute < 10

-- 에러




-- 에러 해결
