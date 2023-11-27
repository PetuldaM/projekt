import csv
import time
from geopy.geocoders import Nominatim

def get_street_name(latitude, longitude):
    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.reverse((latitude, longitude), language="en")

    if location and location.address:
        # Extract the street name from the address
        address_components = location.raw.get("address", {})
        street_name = address_components.get("road", None)

        return street_name

    return None

with open('nehodyupr2018.csv', 'r', encoding='utf-8') as inputfile:
    accidents = inputfile.read().splitlines()

for accident in accidents[34500:36000]:
    accident_split = accident.split(',')
    latitude = accident_split[5]   
    longitude = accident_split[6]
    street_name = get_street_name(latitude, longitude)
    new_accident = [accident_split[1], latitude, longitude, street_name]

    with open('ulice2018.csv', mode='a', encoding= 'UTF-8', newline='') as output_file:
            csv_zapis = csv.writer(output_file)
            csv_zapis.writerow(new_accident)
    time.sleep(1)
