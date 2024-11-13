USE world;
SELECT * FROM Country LIMIT 1000;

SELECT Name, Continent, Population 
FROM Country 
WHERE Continent = 'Asia' AND Population > 50000000;

SELECT Country.Name AS Country, City.Name AS LargestCity, City.Population 
FROM Country 
JOIN City ON Country.Code = City.CountryCode 
ORDER BY City.Population DESC 
LIMIT 10;

SELECT Continent, SUM(Population) AS TotalPopulation 
FROM Country 
GROUP BY Continent;

INSERT INTO Country (Code, Name, Continent, Region, SurfaceArea, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadofState, Capital) 
VALUES ('PK', 'Pakistan', 'Asia', 'Southern Asia', 881913, 207774520, 67.6, 284000, 298600, 'پاکستان', 'Federal Republic', 'Arif Alvi', 1);

SELECT * FROM Country WHERE Code = 'PK';

# adding country code 
CREATE TABLE phonecodes (
    country_code CHAR(2) PRIMARY KEY,
    phone_code VARCHAR(10) NOT NULL
);

INSERT INTO phonecodes (country_code, phone_code) VALUES
('PK', '+92'),
('US', '+1'),
('IN', '+91');

