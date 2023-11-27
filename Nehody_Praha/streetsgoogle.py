'''
Popis - tento skript doplňuje názvy ulic u souřadnic, kde se nepovedlo získat je z Openstreetmap, přesto pár souřadnic zůtsává nedoplněných, bude doplněno ručně.

'''

import requests
import csv
import key_api # Pro možnost stahování je potřeba vygenerovat api key přímo na stránkách google maps pod uživatelským jménem. Klíč mám uložený lokálně v samostatném souboru

def get_street_name(api_key, latitude, longitude):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"{latitude},{longitude}",
        "key": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["status"] == "OK":
        result = data["results"][0]
        address_components = result.get("address_components", [])

        for component in address_components:
            if "route" in component.get("types", []):
                return component["long_name"]

    return None

# načtení api klíče ze samostatného souboru
api_key = key_api.api_key_google

# otevření zdrojového souboru s ulicemi 

with open('ulice2018.csv', 'r', encoding='utf-8') as inputfile:
    accidents = inputfile.read().splitlines()


for accident in accidents:
    accident_detail = accident.split(',')
    latitude = accident_detail[1]
    longitude = accident_detail[2]
    street_name = accident_detail[3]
    if street_name == '':    
        street_name = get_street_name(api_key, latitude, longitude)
        accident_detail[3] = street_name   
    

    with open('ulice2018_new.csv', 'a', encoding='UTF 8', newline='') as output_file:
        csv_zapis = csv.writer(output_file, delimiter = ';') 
        csv_zapis.writerow(accident_detail)