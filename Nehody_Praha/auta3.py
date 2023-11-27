'''
Skript slouží k vytvoření csv souboru se seznamem aut
'''

from typing import Any, Dict, List
import json
import sys
import csv

if len(sys.argv) < 2:
    print("nezadany argument, zadejte jeden nebo vice roku v rozmezi let 2017 - 2023")
    exit()

for rok in sys.argv[1:]:

    vstupni_soubor = f'accidents{rok}.json'
    vystupni_soubor = f'auta{rok}.csv'

    with open(vstupni_soubor, encoding='UTF-8') as file:
        accidents: List[Dict[str, Dict[str, Any]]] = json.load(file)

    # zahlavi sloupcu
    header = ['id_nehoda', 'cislo_auta', 'druh_vozidla', 'znacka', 'skoda', 'pneumatiky', 'kategorie_ridic', 'stari_vozidla', 'vlastnik', 'vzdelani_ridice', 'delka_praxe', 'stav_ridice', 'ovlivneni_ridice', 'oznaceni', 'pohlavi_ridice', 'vek_ridice', 'statni_prislusnost']

    oddelovac = ';'
    csv_zapis = csv.writer(open(vystupni_soubor, mode='w', encoding= 'UTF-8', newline=''), delimiter = oddelovac) 
    csv_zapis.writerow(header)

    # list s označením klíčů, jejichž hodnoty je potřeba uložit do csv souboru
    sloupce = [
        'Druh vozidla',
        'Výrobní značka',
        'Škoda na vozidle (Kč)',
        'Druh pneumatik na vozidle',
        'Kategorie řidiče',
        'Stáří vozidla (roky)',
        'Charakteristika (vlastník)',
        'Nejvyšší ukončené vzdělání',
        'Délka řidičské praxe v řízení (roky)',
        'Stav řidiče',
        'Vnější ovlivnění řidiče',
    ]

    # procházení jednotlivých nehod a vytvoření záznamu do csv souboru, využití slovníku klíčů
    for accident in accidents:
        id_nehoda, nehoda = accident.popitem()
        keys_main = list(nehoda.keys())
        cislo_auta = 0
        for auto in keys_main[2:]:
            cislo_auta += 1
            data = [id_nehoda, str(cislo_auta)]
            for sloupec in sloupce:
                data.append(nehoda[auto][sloupec])
            # vyhledání řidíčů a získání informací o řidiči.
            for key in nehoda[auto]:
                if not key.startswith("person-") or nehoda[auto][key]['Označení'] != "řidič":
                    continue
                person = nehoda[auto][key]
                for personkey in (
                    'Označení',
                    'Pohlaví',
                    'Věk',
                    'Státní příslušnost',                
                ):
                    data.append(person[personkey])
        # pridani noveho zaznamu do csv souboru    
        csv_zapis.writerow(data)  