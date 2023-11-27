-- Připojení kalendáře k tabulkám nehod

CREATE OR REPLACE TABLE NEHODY AS
SELECT 
      k."datum" AS kdatum
    , "den_v_tydnu"
    , "pracovni_den"
    , "prazdniny"
    , n.* 
FROM nehody_celek AS n
LEFT JOIN "kalendar" AS k ON n."datum" = kdatum;

-- SPojení tabulek Nehod a aut

create or replace table NEHODY_FINAL AS
SELECT *
FROM NEHODY_KATEGORIZACE as t1
LEFT JOIN AUTA_KATEGORIZACE as t2 ON t1."id" = t2."id_nehoda";