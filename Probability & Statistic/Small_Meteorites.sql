SELECT 
name,
id,
nametype,
classification,
SUBSTRING(SUBSTRING(mass,10),length(SUBSTRING(mass,10))-9,-length(SUBSTRING(mass,10))) AS mass,
fall,
CASE WHEN length(year) IS 4 THEN YEAR ELSE SUBSTRING(year,8,4) END AS year,
SUBSTRING(SUBSTRING(coordinates,14),length(SUBSTRING(coordinates,14))-1,-length(SUBSTRING(coordinates,14))) AS coordinates
FROM MeteoriteData_Sheet1 
WHERE MASS is not '' OR mass < 50001
