'''
Tento skript generuje csv soubory ze souboru json za jednotlive roky o jednotlivych nehodach. Pomoci argumentu je mozne zadat vsechny roky, ktere jsou dostupne ve formatu json.

'''



import json
import sys
import geopandas as gpd
from shapely.geometry import Point
import csv

# Pokud je program spusten bez argumentu (1 - vice roku), ukonci se a upozorni uzivatele na chybejici argument 
if len(sys.argv) < 2:
    print("nezadany argument, zadejte jeden nebo vice roku v rozmezi let 2017 - 2023")
    exit()

# nacteni souboru geojson s polygony jednotlivych mestskych casti

districts = gpd.read_file('TMMESTSKECASTI.json')

# prochazi jednotlive roky - doplni se rok do nazvu vstupnich i vystupnich souboru a ciselne oznaceni roku
for rok in sys.argv[1:]:

    vstupni_soubor = f'accidents{rok}.json'
    vystupni_soubor = f'nehody{rok}.csv'
    
    with open(vstupni_soubor, encoding='UTF-8') as file:
        accidents = json.load(file)

    # zahlavi sloupcu
    header = ['rok', 'id', 'datum', 'cas', 'druh_nehody', 'latitude', 'longitude', 'mestska_cast', 'stav_komunikace', 'pocasi', 'viditelnost', 'charakter_nehody', 'vina', 'alkohol', 'drogy', 'pricina', 'usmrceno_osob', 'tezce_zraneno', 'lehce_zraneno', 'pocet_vozidel', 'celkova_skoda', 'povrch_vozovky', 'stav_vozovky', 'misto_nehody']

    oddelovac = ';'
    csv_zapis = csv.writer(open(vystupni_soubor, mode='w', encoding= 'UTF-8', newline=''), delimiter = oddelovac) 
    csv_zapis.writerow(header)


    # data za jednotlive nehody
    for accident in accidents:
        id = list(accident.keys())[0]
        table_main = accident[id]['tableMain']
        table_detail = accident[id]['tableDetail']
        datum_cas = table_main['Datum']
        # "17.10.2017 (úterý), 10:40" -> ["17", "10", "2017"]
        datum_vychozi = datum_cas.split(' ')[0].split('.')
        # ["17", "10", "2017"] -> "2017-10-17"
        datum = datum_vychozi[2] + '-' + datum_vychozi[1] + '-' + datum_vychozi[0] # prevod datumu na format Snowflaku, pro dalsi zpracovani dat
        # "17.10.2017 (úterý), 10:40" -> "10:40"
        cas_vychozi = datum_cas.split(' ',2)[-1]
        if cas_vychozi == 'čas neznámý':
            cas = 'čas neznámý'
        elif cas_vychozi.split(':')[1] == '??': # uprava casu, kde nejsou znamy konkretni minuty na format hh:30
            cas = cas_vychozi.split(':')[0] + ':30'
        else:
            cas = cas_vychozi
        druh_nehody = table_main['Druh nehody']
        latitude  = table_main['gps']['lat']
        longitude = table_main['gps']['lng']
        # ziskani nazvu MC na zaklade souradnic
        district = "Neznámá MĆ"
        accident_point = Point(longitude, latitude)
        for index, district_area in districts.iterrows():
            if accident_point.within(district_area['geometry']):
                district = district_area['NAZEV_MC']
        stav_komunikace = table_detail['Stav komunikace']
        pocasi = table_detail['Povětrnostní podmínky v době nehody']
        viditelnost = table_detail['Viditelnost']
        charakter_nehody = table_detail['Charakter nehody']
        vina = table_detail['Zavinění nehody']
        alkohol = table_detail['Přítomnost alkoholu u viníka nehody']
        drogy = table_detail['Přítomnost drog u viníka nehody']
        pricina = table_detail['Hlavní příčina nehody']
        usmrceno_osob = int(table_detail['Usmrceno osob'])
        tezce_zraneno = int(table_detail['Těžce zraněno osob'])
        lehce_zraneno = int(table_detail['Lehce zraněno osob'])
        pocet_vozidel = int(table_detail['Počet zúčastněných vozidel'])
        celkova_skoda = int(table_detail['Celková hmotná škoda (Kč)'])
        povrch_vozovky = table_detail['Druh povrchu vozovky']
        stav_vozovky = table_detail['Stav povrchu vozovky v době nehody']
        misto_nehody = table_detail['Místo dopravní nehody']
        
        # pridani noveho zaznamu do transformovaneho souboru
        zaznam = [rok, id, datum, cas, druh_nehody, latitude, longitude, district, stav_komunikace, pocasi, viditelnost, charakter_nehody, vina, alkohol, drogy, pricina, usmrceno_osob, tezce_zraneno, lehce_zraneno, pocet_vozidel, celkova_skoda, povrch_vozovky, stav_vozovky, misto_nehody]
        csv_zapis.writerow(zaznam)