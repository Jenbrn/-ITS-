import os, json, random
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path

if not os.path.exists('data'):
    os.mkdir('data')
if not os.path.exists('report'):
    os.mkdir('report')
if not os.path.exists('data/input'):
    os.makedirs('input', exist_ok=True)
if not os.path.exists('data/output'):
    os.makedirs('output', exist_ok=True)
if not os.path.exists('data/backup'):
    os.makedirs('backup', exist_ok=True)

# if not os.path.exists('studenti.py'):
#     os.makedirs('studenti.py', exist_ok=True)

if not os.path.exists('config.json'):
    with open("config.json", "w", encoding="utf-8") as f:
        f.write("""{
"numero_studenti": 5,
"voto_min": 2,
"voto_max": 10,
"materie": ["Matematica", "Informatica", "Italiano"],
"classe": "5A",
"nomi": ["Andrea", "Luigi", "Mario", "Alex", "Peppe"],
"cognomi": ["Rosso", "Sesto", "Bianchi", "Simonetti", "Decaro"]
}
""")
        

with open("config.json", "r", encoding= "utf-8") as f:
    config = json.load(f)

#funz ausiliarie

def genera_voti(config):
    voti = {}

    for materia in config["materie"]:
        voti[materia] = random.randint(config["voto_min"], config["voto_max"])
    return voti


def gen_data():
    data_inizio = datetime(2004, 1, 1)
    data_fine = datetime(2009, 12, 31)

    diff_giorni = (data_fine - data_inizio).days
    giorni = random.randint(0, diff_giorni)
    data_nascita = data_inizio + timedelta(days=giorni)

    return data_nascita.strftime("%Y-%m-%d")

def gen_email(nome, cognome):
    return f"{nome.lower()}.{cognome.lower()}@scuola.it"




@dataclass
class Studente:
    id: int
    nome: str
    cognome: str
    data_nascita: str
    email: str
    voti: dict

def genera_studenti(config):
    studenti = []

    for id_studente in range(1, config["numero_studenti"] +1 ):
        nome = random.choice(config["nomi"])
        cognome = random.choice(config["cognomi"])

        studente = Studente(
            id = id_studente,
            nome = nome,
            cognome = cognome,
            data_nascita = gen_data(),
            email = gen_email(nome, cognome),
            voti = genera_voti(config)
        )

        studenti.append(asdict(studente))

    return studenti

# studenti = genera_studenti(config)

Path("convert_stud_csv.py").touch()