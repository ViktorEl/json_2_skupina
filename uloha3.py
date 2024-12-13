
import json

kamil = ['Kamil', 'Snaživý', 250]
lenka = ['Lenka', 'Múdra', 200]
odmeny = [kamil, lenka]

with open('odmeny.json', 'w', encoding='utf-8') as f:
    json.dump(odmeny, f)

with open('odmeny.json', 'r', encoding='utf-8') as f:
    print(json.load(f))