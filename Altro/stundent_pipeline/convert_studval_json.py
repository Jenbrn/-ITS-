from Altro.stundent_pipeline.lettura_validazione import studenti_validi, lettura_csv
import json

dati = studenti_validi

def convert_cvs_json(dati, nome_json):
    with open(nome_json, "w") as f:
        json.dump(dati, f, indent=4 )

convert_cvs_json(dati, "output/studenti_validi.json")
