from Altro.stundent_pipeline.esercitazione import config, genera_studenti
import csv
import datetime
import pathlib

studenti = genera_studenti(config)

def estrai(studenti):
    studenti_new = []

    for studente in studenti:
        new_studente = {}
        new_studente["id"] = studente["id"]
        new_studente["nome"] = studente["nome"]
        new_studente["cognome"] = studente["cognome"]
        new_studente["data_nascita"] = studente["data_nascita"]
        new_studente["email"] = studente["email"]
       
        voti = studente["voti"]
        for materia, voto in voti.items():
            new_studente[materia] = voto
        
        studenti_new.append(new_studente)
    
    return studenti_new

def main():
    dat = estrai(studenti)

    #genero timestamp
    with open("studenti.csv", "w") as f:
        fieldnames = ["id", "nome","cognome","data_nascita","email","Matematica","Informatica","Italiano"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dat)

if __name__ == '__main__':
    main()



        

    
