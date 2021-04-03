SELECT 
name,--my first commit
id,
nametype,
classification,
SUBSTRING(SUBSTRING(mass,10),length(SUBSTRING(mass,10))-9,-length(SUBSTRING(mass,10))) AS mass, --To keep only the vaue of the mass
fall,
CASE WHEN length(year) IS 4 THEN YEAR ELSE SUBSTRING(year,8,4) END AS year,--To keep only the year
SUBSTRING(SUBSTRING(coordinates,14),length(SUBSTRING(coordinates,14))-1,-length(SUBSTRING(coordinates,14))) AS coordinates --To keep only coordinates
FROM MeteoriteData_Sheet1 
WHERE MASS is not '' -- To remove null masses
