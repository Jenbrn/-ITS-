import csv, re, collections
from pathlib import Path

def lettura_csv(file_csv) -> list:
    with open(file_csv, mode="r", newline="", encoding= "utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
    
studenti = lettura_csv("studenti.csv")

#Funzioni per il controllo

#scorro studenti e divido mail valide e non
def valida_mail(studenti):
    valide = [studente for studente in studenti if re.match(r".+@.+\..+", studente["email"])]
    scartate = [(studente, "email_invalida") for studente in studenti if not re.match(r".+@.+\..+", studente["email"])]
    return valide, scartate

# separo voti e li scorro per verificare
def valida_voto(studenti):
    validi = []
    scartati = []
    for studente in studenti:
        matematica = int(studente["Matematica"])
        informatica = int(studente["Informatica"])
        italiano = int(studente["Italiano"])

        voto_val = True
        for voto in [matematica, informatica, italiano]:
            if voto < 2 or voto > 10:
                scartati.append(studente, "voto_out_of_range")
                voto_val = False
                
        if voto_val:
            validi.append(studente)
    return validi, scartati

#scorro studenti e valido data
def valida_data(studenti):
    valide = [studente for studente in studenti if re.match(r"^\d{4}-\d{2}-\d{2}$",studente["data_nascita"])]
    scartate = [(studente, "data_invalida") for studente in studenti if not re.match(r"^\d{4}-\d{2}-\d{2}$",studente["data_nascita"])]
    return valide, scartate

def main():
    mail_ok, mail_err = valida_mail(studenti)
    voti_ok, voti_err = valida_voto(mail_ok)
    date_ok, date_err = valida_data(voti_ok)
    errori = mail_err + voti_err + date_err
    conteggio = collections.Counter(errori)
    
    if len(conteggio) != 0:
        
        for errori, count in conteggio.items():
            print(f"{errori}: {count}")
    return date_ok

studenti_validi = main() 

if __name__ == '__main__':
    Path("convert_studval_json.py").touch()
    main()