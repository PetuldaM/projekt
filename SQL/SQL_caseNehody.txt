CREATE OR REPLACE TABLE NEHODY_KATEGORIZACE AS
( 
SELECT *, 
    (CASE
        WHEN "pricina" in ('jiný druh nesprávného způsobu jízdy', 'nezaviněná řidičem', 'chodci na vyznačeném přechodu', 'protijedoucímu vozidlu při objíždění překážky', 'tramvají, která odbočuje', 'nehoda při provádění služebního zákroku (pronásledování pachatele atd.)', 'nehoda v důsledku  použití (policií) prostředků k násilnému zastavení vozidla (zastavovací pásy, zábrana, vozidlo atp.)') THEN 'jiné'
        WHEN "pricina" in ('řidič se plně nevěnoval řízení vozidla ', 'nezvládnutí řízení vozidla', 'samovolné rozjetí nezajištěného vozidla', 'bezohledná, agresivní, neohleduplná jízda', 'při předjíždění došlo k ohrožení předjížděného řidiče vozidla (vynucené zařazení, předjížděný řidič musel prudce brzdit, měnit směr jízdy apod.)', 'vjetí na nezpevněnou komunikaci', 'náhlé bezdůvodné snížení rychlosti jízdy, zabrzdění nebo zastavení', 'přehlédnutí již předjíždějícícho souběžně jedoucího vozidla') THEN 'nepozornost a bezohlednost'
        WHEN "pricina" in ('nepřizpůsobení rychlosti stavu vozovky (náledí, výtluky, bláto, mokrý povrch apod.)', 'nepřizpůsobení rychlosti dopravně technickému stavu vozovky (zatáčka, klesání, stoupání, šířka vozovky apod.)', 'nepřizpůsobení rychlosti vlastnostem vozidla a nákladu', 'nepřizpůsobení rychlosti intenzitě (hustotě) provozu', 'jiný druh nepřiměřené rychlosti', 'nepřizpůsobení rychlosti viditelnosti (mlha, soumrak, jízda v noci na tlumená světla apod.)', 'nepřizpůsobení rychlosti bočnímu, nárazovému větru (i při míjení, předjíždění vozidel)') THEN 'nepřizpůsobení rychlosti'
        WHEN "pricina" in ('nesprávné otáčení nebo couvání', 'při odbočování vlevo', 'při otáčení nebo couvání', 'při odbočování vlevo souběžně jedoucímu vozidlu', 'při vjíždění na silnici', 'při zařazování do proudu jedoucích vozidel ze stanice, místa zastavení nebo stání', 'chyby při udání směru jízdy') THEN 'otáčení, couvání, odbočování apod.' 
        WHEN "pricina" in('proti příkazu dopravní značky DEJ PŘEDNOST', 'vozidlu přijíždějícímu zprava', 'jízda na “červenou“ 3-barevného semaforu', 'proti příkazu dopravní značky STŮJ DEJ PŘEDNOST', 'jiné nedání přednosti', 'jízda (vjetí) jednosměrnou ulicí, silnicí (v protisměru)', 'překročení předepsané rychlosti stanovené pravidly', 'překročení rychlosti stanovené dopravní značkou')  THEN 'porušení pravidel'
        WHEN "pricina" in ('při přejíždění z jednoho jízdního pruhu do druhého', 'jízda po nesprávné straně vozovky, vjetí do protisměru', 'předjíždění vlevo vozidla odbočujícího vlevo', 'předjíždění bez dostatečného bočního odstupu', 'při předjíždění došlo k ohrožení protijedoucího řidiče vozidla (špatný odhad vzdálenosti potřebné k předjetí apod.)', 'předjíždění vpravo', 'jiný druh nesprávného předjíždění', 'předjíždění bez dostatečného rozhledu (v nepřehledné zatáčce nebo její blízkosti, před vrcholem stoupání apod.)', 'při předjíždění byla přejeta podélná čára souvislá', 'bránění v předjíždění', 'předjíždění v místech, kde je to zakázáno dopravní značkou') THEN 'přejíždení mezi pruhy a předjíždění'
        WHEN "pricina" in ('nesprávné uložení nákladu', 'upadnutí, ztráta kola vozidla (i rezervního)', 'jiná technická závada (vztahuje se i na přípojná vozidla)', 'defekt pneumatiky způsobený průrazem nebo náhlým únikem vzduchu', 'závada provozní brzdy', 'závada závěsu pro přívěs', 'utržená spojovací hřídel', 'závada řízení', 'nepřipojená nebo poškozená spojovací hadice pro bzrdění přípojného vozidla', 'neúčinná nebo nefungující parkovací brzda', 'nezajištěná nebo poškozená bočnice (i u přívěsu)', 'lom závěsu kola, pružiny', 'opotřebení běhounu pláště pod stanovenou mez') THEN 'technická závada'
        WHEN "pricina" in ('nedodržení bezpečné vzdálenosti za vozidlem', 'vyhýbání bez dostatečného bočního odstupu (vůle)')  THEN 'nedodržení bezpečné vzdálenosti'
        else '1'
    end) as "pricina2",
    (CASE
        WHEN try_to_time("cas", 'HH24:MI') BETWEEN '07:00' AND '10:00' THEN 'spicka'
        WHEN try_to_time("cas", 'HH24:MI') BETWEEN '15:00' AND '19:00' THEN 'spicka'
        WHEN try_to_time("cas", 'HH24:MI') BETWEEN '06:00' AND '07:00' THEN 'mimo spicku'
        WHEN try_to_time("cas", 'HH24:MI') BETWEEN '10:01' AND '14:59' THEN 'mimo spicku'
        WHEN try_to_time("cas", 'HH24:MI') BETWEEN '19:00' AND '22:00' THEN 'mimo spicku'
        WHEN try_to_time("cas", 'HH24:MI') BETWEEN '22:01' AND '23:59' THEN 'nocni provoz'
        WHEN try_to_time("cas", 'HH24:MI') BETWEEN '00:00' AND '05:59' THEN 'nocni provoz'
        ELSE 'čas neznámý'
  END) AS "cas2"
FROM nehody);