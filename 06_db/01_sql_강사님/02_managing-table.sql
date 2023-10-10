CREATE TABLE examples (
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

PRAGMA table_info('examples');

ALTER TABLE 
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL
DEFAULT
  '부산';


ALTER TABLE
  examples
ADD COLUMN
  Age INTEGER NOT NULL;

ALTER TABLE
  examples
ADD COLUMN
  Address VARCHAR(100) NOT NULL;
-- [오후 3:27:02][vscode-sqlite][ERROR] 
-- Cannot add a NOT NULL column with 
-- default value NULL

-- 컬럼 명 수정
-- Address -> PostCode
ALTER TABLE
  examples
RENAME COLUMN
  Address TO PostCode;

ALTER TABLE
  examples
DROP COLUMN
  PostCode;

ALTER TABLE 
  examples
RENAME TO 
  new_examples;

ALTER TABLE
  new_examples
RENAME TO
  examples;

DROP TABLE examples;