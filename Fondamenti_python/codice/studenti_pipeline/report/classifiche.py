import sys
from pathlib import Path
from statistics import mean
from collections import namedtuple
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# from lettura_validazcsv import studenti_validi

# STEP 7 - Classifiche studenti (TOP 5 migliori)

# Definire una namedtuple per organizzare meglio i dati
Risultato = namedtuple('Risultato', ['nome', 'email', 'media', 'matematica', 'informatica', 'italiano'])


def calcola_media_studenti(studenti):
   
    risultati = []
    
    for studente in studenti:
        # Estrai i voti
        matematica = int(studente["Matematica"])
        informatica = int(studente["Informatica"])
        italiano = int(studente["Italiano"])
        
        # Calcola la media usando statistics.mean()
        media = mean([matematica, informatica, italiano])
        
        # Crea il risultato come namedtuple
        risultato = Risultato(
            nome=studente["nome"],
            email=studente["email"],
            media=round(media, 2),
            matematica=matematica,
            informatica=informatica,
            italiano=italiano
        )
        
        risultati.append(risultato)
    
    # Ordina per media (decrescente)
    risultati_ordinati = sorted(risultati, key=lambda x: x.media, reverse=True)
    
    return risultati_ordinati


def get_top_5_sorted(studenti):

    risultati = calcola_media_studenti(studenti)
    return risultati[:5]

def elabora_studenti(studenti):
    risultati = calcola_media_studenti(studenti)
    top_5 = risultati[:5]
    return risultati, top_5

def intestazione(f, titolo):
    f.write(f"\n{'='*40}\n")
    f.write(f"{titolo}\n")
    f.write(f"{'='*40}\n")

def scrivi_top(f, top_5):
    intestazione(f, "TOP 5 STUDENTI")
    f.write(f"{'Pos':<5} {'Nome':<20} {'Email':<30} {'Media':<8} {'Mat':<6} {'Inf':<6} {'Ita':<6}\n")

    for indice, studente in enumerate(top_5, 1):
        f.write(f"{indice:<5} {studente.nome:<20} {studente.email:<30} {studente.media:<8} {studente.matematica:<6} {studente.informatica:<6} {studente.italiano:<6}\n")


def salva_rep(config, studenti_validi, top_5, statistiche_materie):
    timestamp = datetime.now().strftime("%Y%m%d")
    output_path = Path("report") / f"report_{timestamp}.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        intestazione(f, "REPORT STUDENTI")
        
        f.write(f"Classe:              {config['classe']}\n")
        f.write(f"Data generazione:    {datetime.now().strftime('%Y%m%d')}\n")
        f.write(f"Studenti totali:     {len(studenti_validi)}\n")
        f.write(f"Studenti validi:     {len(studenti_validi)}\n")

        scrivi_top(f, top_5)

        intestazione(f, "STATISTICHE PER MATERIA")
        for materia, stats in statistiche_materie.items():
                f.write(f"{materia}:\n")
                f.write(f"  Media:     {stats['media']}\n")
                f.write(f"  Mediana:   {stats['mediana']}\n")
                f.write(f"  Min - Max: {stats['min']} - {stats['max']}\n")
                f.write(f"  StDev:     {stats['stdev']}\n\n")
