from lettura_validazcsv import studenti_validi
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "data" / "output"

dati = studenti_validi

def convert_cvs_json(dati, nome_json):
    with open(nome_json, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False )

output_file = OUTPUT_DIR / "studenti_validi.json"


convert_cvs_json(dati, output_file)
