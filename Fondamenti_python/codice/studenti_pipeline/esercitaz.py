import os, json, random
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path


def config():
#genero struttura dir

    cartelle = ['data/input','data/output','data/backup','report', 'config']

    for cartella in cartelle:
        os.makedirs(cartella, exist_ok=True)

    # step 1 - creazione config.json
    if not os.path.exists('config/config.json'):
        with open("config/config.json", "w", encoding="utf-8") as f:
            f.write("""{
    "numero_studenti": 30,
    "voto_min": 2,
    "voto_max": 10,
    "materie": ["Matematica", "Informatica", "Italiano"],
    "classe": "5A",
    "nomi": ["Andrea", "Stefano", "Olga", "Sara", "Chiara", "Marco", "Michele", "Alessandro", "Matteo", "Tommaso", "Luigi", "Mario", "Alex", "Peppe", "Carlo", "Ivan"],
    "cognomi": ["Rosso", "Sesto", "Bianchi", "Simonetti", "Decaro", "Vanetti", "Sacco", "Timo", "Ronco", "Micheli", "Fulgori", "Gallo", "Rossi", "Verdi", "Neri", "Ferrari"]
    }
    """)
            
    with open("config/config.json", "r", encoding= "utf-8") as f:
        config = json.load(f)
    return config

# finz ausiliarie

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

# creazione studenti random

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

# Path("convert_stud_csv.py").touch()