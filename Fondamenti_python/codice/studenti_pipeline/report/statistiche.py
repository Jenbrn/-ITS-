import statistics, math, sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# from lettura_validazcsv import studenti_validi

def estraz(studenti):
    materie = ["Matematica", "Informatica", "Italiano"]
    return {materia : [int(voto[materia]) for voto in studenti] for materia in materie}
    
    # matematica = [int(voto["Matematica"]) for voto in studenti_validi]

    # informatica = [int(voto["Informatica"]) for voto in studenti_validi]

    # italiano = [int(voto["Italiano"]) for voto in studenti_validi]


# print(matematica, informatica, italiano)
def calcoli_statistche(materia):
    media = round(statistics.mean(materia), 1)
    mediana = round(statistics.median(materia), 1)
    stdev = round(statistics.stdev(materia),1)
    minimo, massimo = (min(materia)), (max(materia))
    return media, mediana, stdev, minimo, massimo

def main(studenti_validi):
    voti_per_materia = estraz(studenti_validi)
    risultati = {}

    for materia, voti in voti_per_materia.items():
        media, mediana, stdev, minimo, massimo = calcoli_statistche(voti)

        risultati[materia] = {
            "media" : media,
            "mediana" : mediana,
            "stdev" : stdev,
            "min" : minimo,
            "max" : massimo
        }
    return risultati

if __name__ == '__main__':
    main()
