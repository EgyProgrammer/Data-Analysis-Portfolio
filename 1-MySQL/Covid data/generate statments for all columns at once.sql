-- Step 1: Replace empty strings with NULL
SELECT CONCAT('UPDATE coviddeaths SET ', COLUMN_NAME, ' = NULL WHERE ', COLUMN_NAME, ' = '''';') AS sql_statement
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'coviddeaths'
  AND TABLE_SCHEMA = 'new_schema'  -- change to your actual database name
  AND DATA_TYPE IN ('varchar', 'char', 'text');

select concat('alter table coviddeaths ','modify column ',column_name,' int;') as sql_statement
from information_schema.columns
where table_name='coviddeaths';