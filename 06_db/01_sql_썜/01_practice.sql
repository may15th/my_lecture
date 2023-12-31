-- 'artists' table 활용

-- 모든 아티스트의 정보를 조회하시오.
SELECT
 *
FROM
 artists;

-- 모든 데이터의 수를 조회하시오.
-- 안됨 방법 찾기

SELECT COUNT(*) AS TotalCount
FROM artists;


-- Name이 'AC/DC' 인 정보를 조회하시오.

SELECT
 *
FROM
 artists
WHERE
 Name = 'AC/DC';

-- 모든 데이터 중, Name만 출력하시오.

SELECT
 Name
FROM
 artists;

-- Name이 'Gilberto Gil' 이거나 'Ed Motta' 정보를 조회하시오.

SELECT
 *
FROM
 artists
WHERE
 Name in ('Gilberto Gil', 'Ed Motta');

-- 모든 정보를 Name 기준으로 내림차순 정렬하여 조회하시오.

SELECT
 *
FROM
 artists
ORDER BY
 Name DESC;

-- 이름이 'Vinícius' 로 시작하는 정보를 조회하시오. 단, 2개까지만 출력되도록 한다.

SELECT
 *
FROM
 artists
WHERE
 Name LIKE 'Vinícius%'
limit 2;

-- 'ArtistId'가 50번부터 70번까지의 데이터를 조회하여 'ArtistId'만 출력하시오.

SELECT
 ArtistId
FROM
 artists
WHERE
 ArtistId
LIMIT 49,21;

SELECT
 ArtistId
FROM
 artists
WHERE
 ArtistId
LIMIT 21 OFFSET 49;



-- 'invoices' table 활용

-- "InvoiceId"와 "InvoiceDate" 열만 선택하여 조회하시오.

--SELECT 문에서는 AND가 아니라 ','  사용 기억
SELECT
 InvoiceId, InvoiceDate
FROM
 invoices;

-- "BillingCountry"값이 'USA'이고 "Total"이 10보다 큰 레코드만 선택하여 조회하시오.

SELECT
 *
FROM
 invoices
WHERE
 BillingCountry = 'USA' AND Total > 10;


-- "BillingCity"가 'London'이거나 'Berlin'인 레코드를 선택하여 조회하시오.
-- 출력 안됨 정상??

-- SELECT
--  *
-- FROM
--  invoices
-- WHERE
--  BillingCity = 'London' OR 'Berlin';

-- 위는 잘못된 SQL문 아래처럼 '필드명= ' 다시 한 번 붙여줘야 한다!!!


 SELECT
 *
FROM
 invoices
WHERE
 BillingCity = 'London' OR BillingCity = 'Berlin';



-- "Total"이 가장 큰 레코드를 선택하여 조회하시오.

SELECT *, MAX(Total)
FROM
 invoices;

-- 집계함수는 SELECT 필드명 다음에 ','붙인 후 사용한다!!!



-- "InvoiceDate"가 2013년 3월 31일 이후이고 "Total"이 3보다 큰 레코드만 선택하여 조하시오.

SELECT
 *
FROM
 invoices
WHERE InvoiceDate >= '2013-03-31' AND Total > 3 ;

-- 날짜 조건문 줄 때는 ''작은따옴표 안에 날짜 넣어서 숫자 조건 주듯이 하면 됌.



-- "BillingCountry"이 'USA'이고 "BillingState"가 'California'이며 "Total"이 10보다 큰 레코드를 선택하여 조회하시오.

SELECT
 *
FROM
 invoices
WHERE BillingCountry = 'USA' AND BillingState = 'CA' AND Total > 10;

-- "BillingCountry"이 'Canada'이고 "BillingState"이 'Ontario'이며 "BillingCity"가 'Toronto'인 레코드를 선택하여 조회

SELECT
 *
FROM
 invoices
WHERE BillingCountry = 'Canada' AND BillingState = 'ON' AND BillingCity = 'Toronto';

-- "InvoiceDate"가 2023년 1월 1일 이전이고 ("Total"이 50보다 크거나 같거나 "BillingCountry"이 'Brazil'인) 레코드를 선택하여 조회하시오.

SELECT *
FROM invoices
WHERE (InvoiceDate < '2023-01-01' AND (Total >= 50 OR BillingCountry = 'Brazil'));


-- "BillingCountry"를 기준으로 그룹화하고, 각 나라별 총 판매액을 계산하여 조회하시오.


SELECT BillingCountry,SUM(Total)
FROM
 invoices
GROUP BY BillingCountry;

-- "InvoiceDate"를 연도별로 그룹화하고, 각 연도별 총 판매액을 계산하여 조회하시오.

-- SELECT YEAR SUM(Total)*******************************
-- FROM
--  invoices
-- WHERE InvoiceDate < '2023-01-01'
-- GROUP BY YEAR(InvoiceDate)
-- ORDER BY YEAR(InvoiceDate);


SELECT
  STRFTIME('%Y', InvoiceDate) AS InvoiceYear,
  SUM(Total) AS TotalSales
FROM invoices
GROUP BY InvoiceYear
ORDER BY InvoiceYear;

--아래것 보다 위에 거가 더 맞는 표현

SELECT
  InvoiceDate AS InvoiceYear,
  SUM(Total) AS TotalSales
FROM invoices
GROUP BY STRFTIME('%Y', InvoiceDate)
ORDER BY InvoiceYear;




-- "BillingCountry"이 'USA'이고 "InvoiceDate"가 2010년 01월 01 이후인 레코드를 "BillingState"를 기준으로 그룹화하고, 각 주별로 총 주문 금액을 계산하여 조회하시오.

SELECT BillingState, SUM(Total)
FROM
 invoices
WHERE BillingCountry = 'USA' AND InvoiceDate >= '2010-01-01'
GROUP BY BillingState;



-- "BillingCountry"이 'Germany'이거나 "BillingCountry"이 'France'인 레코드를 "BillingCountry"를 기준으로 그룹화하고, 각 나라별로 최대 주문 금액을 계산하여 조회하시오.

SELECT BillingCountry, MAX(Total)
FROM
 invoices
WHERE BillingCountry = 'Germany' OR BillingCountry = 'France'
GROUP BY BillingCountry;