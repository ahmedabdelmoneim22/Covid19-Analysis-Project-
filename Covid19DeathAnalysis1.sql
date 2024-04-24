-->>Covid 19 Death Analysis Project.
-->>AggregateFunctions,WindowsFunctions,CreatingViews,Converting Data Types,Joins;
/*
1.Print ALL CovidDeaths Table;
>>in condition continent Column Not Null;
Order By Column 3,Column 4;
*/
Select *
From Covid19Project.dbo.CovidDeaths
Where continent is not null 
order by 3,4
/*
2.Print Columns I Will Use in Analysis;
*/
Select Location, date, total_cases, new_cases, total_deaths, population
From Covid19Project.dbo.CovidDeaths
Where continent is not null 
order by 1,2
/*
-->>Total-Cases vs Total-Deaths.
-->>Shows likelihood of Dying. 
-->>if you contract covid in your country.
Percentage Covid 19 Dying InTo Your Country.
*/
-->>Convert The DataType To Solve The Error.
Alter Table Covid19Project.dbo.CovidDeaths Alter COLUMN total_cases Float
Alter Table Covid19Project.dbo.CovidDeaths Alter COLUMN total_deaths Float
-->>Calculate Death % Percentage in Your-Country.
Select Location, date, population,total_cases,total_deaths,(total_deaths/total_cases)*100 as DeathPercentage
From Covid19Project.dbo.CovidDeaths
Where location like '%Egypt%' and continent is not null 
order by 1,2
/*
-->>Total Cases vs Population.
-->>Shows What Percentage of (population infected with Covid).
-->>Percent Population Infected in Your Country. 
*/
Select Location, date, Population, total_cases,  (total_cases/population)*100 as PercentPopulationInfected
From Covid19Project.dbo.CovidDeaths 
Where location like '%Egypt%'
order by 1,2
/*
-->>Countries with Highest Infection Rate. 
-->>Compared to Population.
*/
Select Location, date, Population, total_cases,  (total_cases/population)*100 as PercentPopulationInfected
From Covid19Project.dbo.CovidDeaths 
order by PercentPopulationInfected DESC
/*
>>Group by with Aggregate Function.
Calculate:-
1>>Highest Infection Count.
2>>Percent Population Infected.
*/
Select Location, Population, MAX(total_cases) as HighestInfectionCount,  Max((total_cases/population))*100 as PercentPopulationInfected
From Covid19Project.dbo.CovidDeaths
Group by Location, Population
order by PercentPopulationInfected DESC
/*
>>Countries With Highest Death.
>>Countries with Highest Death Count per Population.
*/
Select Location, Population, MAX(total_deaths) as HighestDeathsCount,  Max((total_deaths/population))*100 as PercentPopulationDeaths
From Covid19Project.dbo.CovidDeaths
Group by Location, Population
order by PercentPopulationDeaths DESC
/*
>>Calculate-Death-Count-Per-Population. 
-->>Total Death Count in Every Country.
*/
Select Location, MAX(cast(Total_deaths as int)) as TotalDeathCount
From Covid19Project.dbo.CovidDeaths
Where continent is not null and location like '%Egypt%'
Group by Location
order by TotalDeathCount DESC
/*
-->>Show Contintents with the Highest Death count per population.
*/
Select * from Covid19Project.dbo.CovidDeaths;
-->>{Calculate Total Death Count in Every Continent}.
Select continent, MAX(cast(Total_deaths as int)) as TotalDeathCount
From Covid19Project.dbo.CovidDeaths
Where continent is not null 
Group by continent
order by TotalDeathCount DESC
/*
>>GLOBAL-Insights.
>>Sum of Total Cases.
>>Sum of Total Deaths.
>>The Percentage of Death.
*/
Select SUM(new_cases) as total_cases, 
	   SUM(cast(new_deaths as int)) as total_deaths, 
	   SUM(cast(new_deaths as int))/SUM(New_Cases)*100 as DeathPercentage
From Covid19Project.dbo.CovidDeaths
where continent is not null and location like '%Egypt%'
order by 1,2
/*
>>Total-Population vs Vaccinations.
>>Shows Percentage of Population that has Recieved at least one Covid-Vaccine.
*/
Select * from Covid19Project.dbo.CovidVaccinations;
/*Print new vaccinations Column*/
Select new_vaccinations
From Covid19Project.dbo.CovidVaccinations;
--CTE & OVER() Clause;
Select death.continent, death.location, death.date, death.population, vac.new_vaccinations
, SUM(CONVERT(Float,vac.new_vaccinations)) OVER  (Partition by death.Location Order by death.location, death.Date) as RollingPeopleVaccinated,
(SUM(CONVERT(Float,vac.new_vaccinations)) OVER (Partition by death.Location Order by death.location, death.Date) /death.population) * 100 as PercentageofRollingPeopleVaccinated
From Covid19Project.dbo.CovidDeaths death
Join Covid19Project.dbo.CovidVaccinations vac
	On death.location = vac.location
	and death.date = vac.date
where death.continent is not null 
order by 2,3
-->>A-Common-Table-Expression-(CTE).
/*
>>Common Table ExpressionCTE.
1.A CTE can be only specified in a SELECT Statement.
2.A CTE can be only specified in a CREATE VIEW Statement.
*/
--START-CTE.
With 
PopulationVsVaccinations
as(
Select death.continent, death.location, death.date, death.population, vac.new_vaccinations
, SUM(CONVERT(Float,vac.new_vaccinations)) OVER  (Partition by death.Location Order by death.location, death.Date) as RollingPeopleVaccinated
,(SUM(CONVERT(Float,vac.new_vaccinations)) OVER (Partition by death.Location Order by death.location, death.Date) /death.population) * 100 as PercentageofRollingPeopleVaccinated
From Covid19Project.dbo.CovidDeaths death
Join Covid19Project.dbo.CovidVaccinations vac
	On death.location = vac.location
	and death.date = vac.date
where death.continent is not null )
Select * 
from PopulationVsVaccinations
order by 2,3
--END-CTE.
/*How The SUM() Function Working.
new_vaccinations RollingPeopleVaccinated PercentageofRolingPeopleVaccinated
2859			 2859					 0.006951
4015	         6874					 0.016713
*/
--START-CTE.
With 
PopulationVsVaccinations
as(
Select death.continent, death.location, death.date, death.population, vac.new_vaccinations
, SUM(CONVERT(Float,vac.new_vaccinations)) OVER  (Partition by death.Location Order by death.location, death.Date) as RollingPeopleVaccinated
,(SUM(CONVERT(Float,vac.new_vaccinations)) OVER (Partition by death.Location Order by death.location, death.Date) /death.population) * 100 as PercentageofRollingPeopleVaccinated
From Covid19Project.dbo.CovidDeaths death
Join Covid19Project.dbo.CovidVaccinations vac
	On death.location = vac.location
	and death.date = vac.date
where death.continent is not null )
Select *,(RollingPeopleVaccinated/population)*100 as PeopleVaccinatedPercentage
from PopulationVsVaccinations
order by 2,3
--END-CTE.
/*>>Create New Table To Insert The Data Into It*/
-->>If Table In DataBase Delete It;
DROP Table if exists Covid19Project.dbo.PercentOfPopulationVaccinated
-->>Create New Table To Insert Into It PopulationVsVaccinations;
Create Table Covid19Project.dbo.PercentOfPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)
-->>INSERT The Data Into TABLE PercentOfPopulationVaccinated;
Insert Into Covid19Project.dbo.PercentOfPopulationVaccinated
Select death.continent, death.location, death.date, death.population, vac.new_vaccinations
, SUM(CONVERT(Float,vac.new_vaccinations)) OVER  (Partition by death.Location Order by death.location, death.Date) as RollingPeopleVaccinated
From Covid19Project.dbo.CovidDeaths death
Join Covid19Project.dbo.CovidVaccinations vac
	On death.location = vac.location
	and death.date = vac.date
where death.continent is not null 
order by 2,3
/*Select The Data From TABLE PercentOfPopulationVaccinated*/
Select * From Covid19Project.dbo.PercentOfPopulationVaccinated
order by 2,3
/*Calculate The Parentage of People That Vaccinated*/
Select *,(RollingPeopleVaccinated/Population) * 100 as PercentOfPeopleVaccinated
from Covid19Project.dbo.PercentOfPopulationVaccinated
where location like '%Egypt%' and Continent is not null
order by 2,3
/*
>>Creating-The-View.
-->>Creating View to Store Data for Later-Visualizations.
Views in SQL offer 
1.Data security, 
2.Hiding complex Query,and 
3.Data consistency.
>>A View in SQL is A Virtual-Table.
*/
Create View PercentOfPopulationVaccinated1 As 
Select death.continent, death.location, death.date, death.population, vac.new_vaccinations
, SUM(CONVERT(Float,vac.new_vaccinations)) OVER  (Partition by death.Location Order by death.location, death.Date) as RollingPeopleVaccinated,
(SUM(CONVERT(Float,vac.new_vaccinations)) OVER (Partition by death.Location Order by death.location, death.Date) /death.population) * 100 as PercentageofRollingPeopleVaccinated
From Covid19Project.dbo.CovidDeaths death
Join Covid19Project.dbo.CovidVaccinations vac
	On death.location = vac.location
	and death.date = vac.date
where death.continent is not null 

Select continent,location,date,population,new_vaccinations,RollingPeopleVaccinated,PercentageofRollingPeopleVaccinated 
from PercentOfPopulationVaccinated1
order by 2,3

Select SUM(new_cases) as total_cases, 
	   SUM(cast(new_deaths as int)) as total_deaths, 
	   SUM(cast(new_deaths as int))/SUM(New_Cases)*100 as DeathPercentage
From Covid19Project.dbo.CovidDeaths
where continent is not null and location like '%Egypt%'
order by 1,2
-------------------------------------------------------
Select SUM(New_vaccinations) as total_Vaccinations,
sum(New_vaccinations/Population) * 100 as PercentOfPeopleVaccinated
from Covid19Project.dbo.PercentOfPopulationVaccinated
where location like '%Egypt%' and Continent is not null
order by 1,2
/*
********************************************
********************************************
*/
Select location
from Covid19Project.dbo.CovidDeaths
group by location
order by location
/*
Continent.
Location.
Date.
Population.
New Vaccinations.
RollingPeopleVaccinated
PercentOfPeopleVaccinated
*/
