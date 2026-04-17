import json

from mod04_csv import leggi_file_csv

def convert_csv_json(nome_file_csv, nome_file_json):
    dati = leggi_file_csv(nome_file_csv)

    with open(nome_file_json, "w") as f:
        json.dump(dati, f, indent=4)

convert_csv_json("moto.csv", "moto.json")
convert_csv_json("auto.csv", "auto.json")
