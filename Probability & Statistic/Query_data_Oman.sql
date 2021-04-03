select 
name,
mass,
coord_x,
coord_y
FROM
(SELECT
name,
mass,
CAST (SUBSTRING(coordinates,-length(coordinates),instr(coordinates,',')-1) as float ) AS coord_x,
CAST (SUBSTRING(coordinates,instr(coordinates,',')+1) as float ) AS coord_y
from
(SELECT 
name,
id,
nametype,
classification,
SUBSTRING(SUBSTRING(mass,10),length(SUBSTRING(mass,10))-9,-length(SUBSTRING(mass,10))) AS mass,
fall,
CASE WHEN length(year) IS 4 THEN YEAR ELSE SUBSTRING(year,8,4) END AS year,
SUBSTRING(SUBSTRING(coordinates,14),length(SUBSTRING(coordinates,14))-1,-length(SUBSTRING(coordinates,14))) AS coordinates
FROM MeteoriteData_Sheet1 
WHERE MASS is not '' OR mass < 50001))
WHERE ((coord_x > 16.7 AND coord_x < 20.02) AND (coord_y > 51.8 AND coord_Y < 57.7)) or 
((coord_x > 20.02 AND coord_x < 25.05 ) AND (coord_y > 55 AND coord_Y < 59.8))
