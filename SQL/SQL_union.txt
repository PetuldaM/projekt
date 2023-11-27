-- Spojení tabulek s nehodami za jednotlivé roky do jedné

Create table NEHODY_CELEK as 
(SELECT *
FROM
    (SELECT * FROM "nehody_vyber2017"
    UNION ALL
    SELECT * FROM "nehody2018"
    UNION ALL
    SELECT * FROM "nehody2019"
    UNION ALL
    SELECT * FROM "nehody2020"
    UNION ALL 
    SELECT * FROM "nehody2021"
    UNION ALL
    SELECT * FROM "nehody2022"
    UNION ALL
    SELECT * FROM "nehody2023"
    )
)
;

-- Spojení tabulek s vozidly za jednotlivé roky do jedné

Create table AUTA as 
(SELECT * FROM
    (SELECT * FROM "auta2017"
    UNION ALL
    SELECT * FROM "auta2018"
    UNION ALL 
    SELECT * FROM "auta2019"
    UNION ALL
    SELECT * FROM "auta2020"
    UNION ALL 
    SELECT * FROM "auta2021"
    UNION ALL
    SELECT * FROM "auta2022"
    UNION ALL
    SELECT * FROM "auta2023"
    )
)
;

select *
from auta;