# najvacsi dodavatel mesta Presov

import json

def nacitaj_json(nazov):
    with open(nazov, 'r', encoding='utf-8') as f:
        nacitany = json.load(f)
        return nacitany

nacitany = nacitaj_json('zoznam_faktury.json')
print(nacitany)