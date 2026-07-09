# extracting month,day and year to remake the date column
with temp_table as(select *,
regexp_substr(date,'[0-9]+') as month,
replace(regexp_substr(date,'/[0-9]+/'),'/','')as day,
regexp_substr(date,'[0-9]{4}') as year
from covidvaccinations
)
select *,str_to_date(concat(month,',',day,',',year),'%m,%d,%y') as new_date
from temp_table
;
# create temporary table to store the data
create temporary table temp_table
with CTE as(select *,
regexp_substr(date,'[0-9]+') as month,
replace(regexp_substr(date,'/[0-9]+/'),'/','')as day,
regexp_substr(date,'[0-9]{4}') as year
from covidvaccinations
)
select *,str_to_date(concat(month,',',day,',',year),'%m,%d,%Y') as new_date
from CTE
;
# recreate the table with the new data
create table covidvaccinations
select * 
from temp_table
;
# modifying the date column
update covidvaccinations
set date=new_date
;
# change the data type of the column
alter table covidvaccinations
modify date date;
# drop the extra columns
alter table covidvaccinations
drop column day,
drop column month,
drop column year,
drop column new_date;



