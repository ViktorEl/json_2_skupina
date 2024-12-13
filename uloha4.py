# najvacsi dodavatel mesta Presov

import json

def nacitaj_json(nazov):
    with open(nazov, 'r', encoding='utf-8') as f:
        nacitany = json.load(f)
        return nacitany



def vytvor_slovnik(zoznam_slovnikov):
    novy_slovnik = {}
    for slovnik in zoznam_slovnikov:
        dodavatel = slovnik['Dodávateľ']
        suma = slovnik['Celková_cena']
        suma = suma.strip()     # odstrani medzery na zaciatku a na konci
        suma = suma.replace(',', '.') # zmena ciarky na bodku
        suma = suma.replace(' ', '') # odstranena medzera medzi cislami
        suma = float(suma)          # pretypovali sme sumu na float
        if dodavatel in novy_slovnik:
            novy_slovnik[dodavatel] += suma
        else:
            novy_slovnik[dodavatel] = suma
    return novy_slovnik




nacitany = nacitaj_json('zoznam_faktury.json')
slovnik_dodavatelov = vytvor_slovnik(nacitany)



