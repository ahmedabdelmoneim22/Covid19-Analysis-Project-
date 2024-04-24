/*
Select *
From CovidProject.dbo.CovidDeath

Select *
from CovidProject.dbo.CovidVaccinations
*/
/*
Indicates sorting by the Third and Fourth Columns;
order by 3,4>>order By Location,date;
 */
 /*Start The Project*/
 --(Print All Columns in Table).
 --Order by Column3,Column4
Select *
From CovidProject.dbo.CovidDeath
order by 3,4
/*----------------------------*/
--Select *
--From CovidProject.dbo.CovidVaccinations
--order by 3,4

--Select Data that We are going to be using.
-->>Print This Columns From Table CovidDeath Order By Column1&Column2.
Select Location,date,total_cases,new_cases,total_deaths,population_density
from CovidProject.dbo.CovidDeath
order by 1,2

-->>(Looking At Total Cases vs Total Deaths).
-->>Using ALTER TABLE To Convert Column DataType,
ALTER TABLE CovidProject.dbo.CovidDeath ALTER COLUMN total_deaths Float;
ALTER TABLE CovidProject.dbo.CovidDeath ALTER COLUMN total_cases Float;
--total_deaths,total_cases>>rightClick>>Modify.
Select Location,date,total_cases,total_deaths,(total_deaths/total_cases)*100 as DeathPercentage
from CovidProject.dbo.CovidDeath
order by 1,2
-->>Get-It-By-Location:-
-->>The Percentage of Dying if Covid in your Country.
Select Location,date,total_cases,total_deaths,(total_deaths/total_cases)*100 as DeathPercentage
from CovidProject.dbo.CovidDeath
Where location like '%Egypt%'
order by 1,2
-->>The Percentage of Dying in United States.
Select Location,date,total_cases,total_deaths,(total_deaths/total_cases)*100 as DeathPercentage
from CovidProject.dbo.CovidDeath
Where location like '%United States%'
order by 1,2
-->>Looking at Total Cases vs Population.
-->>Shows What Percentage of Population got Covid.  
Select Location,date,total_cases,population_density,(total_cases/population_density)*100 as DeathPercentage
from CovidProject.dbo.CovidDeath
Where location like '%United States%'
order by 1,2

--Add Number of Population Column to Table location='United States of America'.
--Alter Table CovidProject.dbo.CovidDeath
--Add population int;
--UPDATE CovidProject.dbo.CovidDeath
--SET population = CASE 
--    WHEN date like '%2020%' AND location = 'United States' THEN 335942003
--	WHEN date like '%2021%' AND location = 'United States' THEN 336997624
--	WHEN date like '%2022%' AND location = 'United States' THEN 338289857
--	WHEN date like '%2023%' AND location = 'United States' THEN 339996563	
--	WHEN date like '%2024%' AND location = 'United States' THEN 341814420
--END;
/*
(781372 rows affected)
Completion time: 2024-04-19T03:16:03.4175376+01:00
*/
Select location,population
from CovidProject.dbo.CovidDeath
Where location='United States'

-->Shows what percentage of populations got Covid.
Select location,date,population,total_cases,(total_cases/population)*100 as DeathPercentage
from CovidProject.dbo.CovidDeath
where location='United States'
order by 1,2

select * from CovidProject.dbo.CovidDeath

Select location
from CovidProject.dbo.CovidDeath
group by location

Select * 
from CovidProject.dbo.CovidDeath

-->>Delete The Column of Population. 
Alter Table CovidProject.dbo.CovidDeath Drop Column population;

-->>Select-All-Columns-In-Table.
Select * from CovidProject.dbo.CovidDeath

Select * from CovidProject.dbo.Population

Alter Table CovidProject.dbo.Population Drop Column F2;
Alter Table CovidProject.dbo.Population Drop Column F3;
Alter Table CovidProject.dbo.Population Drop Column F4;

Select * 
from CovidProject.dbo.Population
-->>ADD New Column>>population of Each Country.  
Alter Table CovidProject.dbo.CovidDeath
Add population int;
-->>Print All Columns From Table CovidDeath.  
Select * from CovidProject.dbo.CovidDeath
-->>Cant Make Update.
-->>Update Column Population With Values;
--Update CovidProject.dbo.CovidDeath
--Set population = (Select  from CovidProject.dbo.CovidDeath).
-->>Merge The Two Tables With INNER JOIN To Solve The Problem.
SELECT *
FROM (SELECT *,ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS rn1 FROM CovidProject.dbo.CovidDeath) as t1
INNER JOIN  (SELECT *,ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS rn2 FROM CovidProject.dbo.Population) as t2
ON t1.rn1=t2.rn2

-->>Create New Table-CovidDeath With population;
Create Table CovidProject.dbo.CovidDeath1(
	ID int
);
--Alter Table CovidProject.dbo.CovidDeath1 Drop Column ID;
Truncate Table CovidProject.dbo.CovidDeath1
Alter Table CovidProject.dbo.CovidDeath Drop Column population
Select *
INTO CovidProject.dbo.CovidDeath2
FROM (SELECT *,ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS rn1 FROM CovidProject.dbo.CovidDeath) as t1
INNER JOIN  (SELECT *,ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS rn2 FROM CovidProject.dbo.Population) as t2
ON t1.rn1=t2.rn2
----------------------------------------------------------------------------------------------------------------
-->>I Will Work on the Table dbo.CovidDeath2 & dbo.CovidVaccinations;
---------------------------
/*
Joins,Window Functions,Aggregate Functions,
Creating Views,Converting Data Type;
*/
--Print All columns in Table Order By Column3,Column4
Select * From CovidProject.dbo.CovidDeath2
where continent is not null
order by 3,4
--******************************************
--Select All Columns you need in Table

Select location,population 
from CovidProject.dbo.CovidDeath2
where location like '%States%'


Select Location, date, total_cases, new_cases, total_deaths, population
From CovidProject.dbo.CovidDeath2
Where continent is not null 
order by 1,2
/************************************************************************/
/*
Our World in Data.
Coronavirus (COVID-19) Deaths.
MicroSoft Office.
Excel.
Insert File One One Drive.
https://ourworldindata.org/covid-deaths
-------------------------------------------------------------
Open With Excel owid-covid-data;
-------------------------------------------------------------
Data Analyst Portfolio Project | SQL Data Exploration | Project 1/4
-------------------------------------------------------------
owid-covid-data.csv Upload To Microsoft 365.
Convert To xlsx File.
Cut Column Poplution.
>>>E.
-----------------------------------------------------------
click>>Ctrl>>Shift>>Right>>Delete.
-----------------------------------------------------
Coronavirus disease (COVID-19).
covid Death.
COVID - Coronavirus Statistics.
 ---------------------------------------------------
Ctrl Shift From Z to E.
----------------------------------------------------
Excel>>Viewing>>Editing.
----------------------------------------------------
Ctrl+Shift>>>Z A>>right Click>>Delete.
---------------------------------------------------
Need To get him into SQL.
---------------------------------------------------
Create New Database >> CovidProject >> Right Click>>Tasks>>Import Data.
MicroSoft Server 2022 Import and Export.
Excel file path:Browse
>>MicroSoft Excel>>
--------------------------------
XLSX to CSV Converter.
--------------------------------
The Percentage of dying if Covid in your Country
Coronavirus (COVID-19) Deaths
COVID - Coronavirus Statistics
---------------------------------
*/
--------------------------------------------------






