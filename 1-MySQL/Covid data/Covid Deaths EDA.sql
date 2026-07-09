select *
from coviddeaths
;
----------------------------------------------------------------------
# Total cases vs deaths
select location,date,total_cases,total_deaths,
total_deaths*100/total_cases as percent_deaths
from coviddeaths
where continent!="" # when there is no continent the location is the continent which gives the entire continent population, in turn gives a wrong caculations
order by location,date
;
----------------------------------------------------------------------
# Percentage of population infected with covid
select location,date,total_deaths,population,
total_deaths*100/population as percent_of_population
from coviddeaths
where continent!=""
;
----------------------------------------------------------------------
# highest infection rate
select location,max(total_cases) as total_cases,population,
max(total_cases)*100/population as percent_infection
from coviddeaths
where continent!=""
group by location,population
order by percent_infection desc
;
----------------------------------------------------------------------
# highest death rate
select location,population,max(total_deaths) as total_deaths,
max(total_deaths)*100/population as percent_death
from coviddeaths
where continent!=""
group by location,population
order by location asc
;
----------------------------------------------------------------------
# total deaths for each continent
with total_continents_deaths as (select continent, location, max(total_deaths) as total_deaths
from coviddeaths
where continent!=""
group by continent,location)
select continent,sum(total_deaths) as total_deaths
from total_continents_deaths
group by continent
order by total_deaths desc
;
----------------------------------------------------------------------
# global numbers
select date,sum(new_cases) as total_cases,sum(new_deaths) as total_deaths,sum(new_deaths)*100/sum(new_cases) as percent_deaths
from coviddeaths
group by date
order by date asc
;
----------------------------------------------------------------------
# join deaths table with vaccinations table
select *
from coviddeaths deaths
join covidvaccinations as vaccs
on deaths.location=vaccs.location and deaths.date=vaccs.date
;
----------------------------------------------------------------------
# population vs vaccination
select deaths.continent,
deaths.location,
deaths.date,
population,new_vaccinations,
sum(new_vaccinations) over (partition by deaths.location order by deaths.location,deaths.date) as running_total
from coviddeaths deaths
join covidvaccinations as vaccs
on deaths.location=vaccs.location and deaths.date=vaccs.date
where deaths.continent!=''
;
----------------------------------------------------------------------
# percentage of vaccinated people
with temp_table (continent,location,date,population,new_vaccinations,running_total) as(
select deaths.continent,
deaths.location,
deaths.date,
population,new_vaccinations,
sum(new_vaccinations) over (partition by deaths.location order by deaths.location,deaths.date) as running_total
from coviddeaths deaths
join covidvaccinations as vaccs
on deaths.location=vaccs.location and deaths.date=vaccs.date
where deaths.continent!=''
)
select continent,location,population,max(running_total) as total_vaccinated_people, 
max(running_total)*100/population as percentage_vaccinated_people
from temp_table
group by continent,location,population;
----------------------------------------------------------------------
# creating percentage of vaccinated people view
drop view if exists percentage_of_vaccinated_people;
create view percentage_of_vaccinated_people as (
with temp_table (continent,location,date,population,new_vaccinations,running_total) as(
select deaths.continent,
deaths.location,
deaths.date,
population,new_vaccinations,
sum(new_vaccinations) over (partition by deaths.location order by deaths.location,deaths.date) as running_total
from coviddeaths deaths
join covidvaccinations as vaccs
on deaths.location=vaccs.location and deaths.date=vaccs.date
where deaths.continent!=''
)
select continent,location,population,max(running_total) as total_vaccinated_people, 
max(running_total)*100/population as percentage_vaccinated_people
from temp_table
group by continent,location,populationcountry_total_deathscountry_total_deaths
);
----------------------------------------------------------------------
# creating total continents deaths view
drop view if exists total_continents_deaths;
create view total_continents_deaths as
(
with total_continents_deaths as (select continent, location, max(total_deaths) as total_deaths
from coviddeaths
where continent!=""
group by continent,location)
select continent,sum(total_deaths) as total_deaths
from total_continents_deaths
group by continent
order by total_deaths desc
);
----------------------------------------------------------------------
# creating country total deaths view
drop view if exists country_total_deaths;
create view country_total_deaths as
(
select location,max(total_deaths) as total_deaths,population,
max(total_deaths)*100/population as percent_death
from coviddeaths
where continent!=""
group by location,population
order by percent_death desc
);
-----------------------------------------------------------------------
# creating Total cases vs deaths view
drop view if exists total_cases_deaths;
create view total_cases_deaths as(
select location,date,total_cases,total_deaths,
total_deaths*100/total_cases as percent_deaths
from coviddeaths
where continent!="" # when there is no continent the location is the continent which gives the entire continent population, in turn gives a wrong caculations
order by location,date)
;




