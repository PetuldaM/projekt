-- Rozdělení tabulky s přehledem aut podle druhu nehody - oddělení nehod se zaparkovaným vozidlem

create or replace table NEHODY_AUTA_BEZ AS
(select *
from join_nehody_auta
where "druh_nehody" NOT ilike '%srážka s vozidlem zaparko%');

-- Rozdělení tabulky s přehledem aut podle druhu nehody - vytvoření nehod se zaparkovaným vozidlem

create or replace table SRAZKA_SE_ZAPARKOVANYM_VOZIDLEM AS
(select * 
from join_nehody_auta
where "druh_nehody" ilike '%srážka s vozidlem zaparko%');