from workalendar.registry import registry
from workalendar.europe import CzechRepublic
from datetime import date, datetime, timedelta
import csv

svatky = CzechRepublic()
start_year = 2017
end_year = 2023

start_date = datetime(2017, 10, 1)
end_date = datetime(2023, 9, 30) 

our_calender = 'datum,den_v_tydnu,pracovni_den,prazdniny'

with open('prazdniny.csv', 'r', encoding='UTF-8') as file:
     prazdniny = file.read().splitlines()

prazdniny_dict = {}
for line in prazdniny:
    line_split = line.split(',')
    prazdniny_dict[line_split[0]] = line_split[1]


for i in range((end_date - start_date).days + 1):
    datum = start_date + timedelta(days = i)
    weekday = datum.strftime('%a')
    working_day = svatky.is_working_day(datum)
    datum2 = datum.strftime('%Y-%m-%d')
    if datum2 in prazdniny_dict.keys():
        if prazdniny_dict[datum2] == 'P1':
            school_holidays = 'Praha 1 - 5'
        elif prazdniny_dict[datum2] == 'P6':
            school_holidays = 'Praha 6 - 10'
        else:
            school_holidays = 'Celá Praha'
    elif weekday == 'Sat' or weekday == 'Sun':
         school_holidays = 'víkend'
    else:
         school_holidays = "škola"



    zaznam = f'{datum2},{weekday},{working_day},{school_holidays}'
    our_calender += f'\n{zaznam}'

with open('kalendar.csv', mode='w', encoding= 'UTF/8') as output_file:
     print(our_calender, file=output_file)