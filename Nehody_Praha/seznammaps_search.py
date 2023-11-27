'''
Skript pro dohledání zbývajících lokací bez názvů ulic. Skript vyhledá souřadnice na serveru mapy.cz a na základě zobrazeného výsledku uživatel zapíše název ulice

'''

import webbrowser
with open('ulice_souradnice.csv', 'r', encoding='utf-8') as file:
    vstup = file.read()

vysledek = []
for lokace in vstup.splitlines():
    sourad = lokace.split(",")
    print(sourad[1] +","+ sourad[2])
    webbrowser.open_new_tab("https://mapy.cz/turisticka?q=" + sourad[1] + "," + sourad[2])   
    sourad[3] = input("Název ulice: ")
    lokace = ""
    for cast in sourad:
        lokace = lokace + cast + ","
        
    vysledek.append(lokace + "\n")
    
    
with open("vysledek.csv", "w", encoding='utf-8') as csv:
    csv.writelines(vysledek)
    
