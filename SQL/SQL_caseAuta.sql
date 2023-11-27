CREATE OR REPLACE TABLE AUTA_KATEGORIZACE AS
( 
SELECT *, 
    (CASE
        WHEN "vek_ridice" < 25 THEN '18-24'
        WHEN "vek_ridice" between 25 and 44 THEN '25-44'
        WHEN "vek_ridice" between 45 and 59 THEN '45-59'
        WHEN "vek_ridice" between 60 and 79 THEN '60-79' 
        WHEN "vek_ridice"  >= 80 THEN '80+'
        else 'ostatni'
    end) as "vek_ridice2",
    (CASE
        WHEN "stari_vozidla" < 4 THEN 'do 3 let'
        WHEN "stari_vozidla" between 4 and 8 THEN '4-8'
        WHEN "stari_vozidla" between 9 and 14 THEN '9-14'
        WHEN "stari_vozidla" between 15 and 20 THEN '15-20' 
        WHEN "stari_vozidla"  >= 20 THEN '20+'
        else 'ostatni'
    end) as "stari_vozidla2",
    (CASE
        WHEN "statni_prislusnost" ilike '%Česká republika%' THEN 'Česká republika'
        WHEN "statni_prislusnost" is null THEN 'null'
        else 'zahraniční'
    end) as "statni_prislusnost2"   
from "AUTA_upravasloupcu")
;