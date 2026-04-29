import sys
from esercitaz import config, genera_studenti
from convert_stud_csv import main as convert_csv_main
from lettura_validazcsv import main as validaz_csv_main
from convert_studval_json import main as converter_cvs_json
from pathlib import Path
from report.statistiche import main as calcoli_statistiche
from report.classifiche import elabora_studenti, salva_rep

def main():
    comando = sys.argv[1]
    if comando == "generate":
        cfg = config()
        studenti = genera_studenti(cfg)
        convert_csv_main(studenti)
        
        
    elif comando == "validate":
        studenti_validi = validaz_csv_main()
        converter_cvs_json(studenti_validi)

        

    elif comando == "all":
        cfg = config()
        studenti = genera_studenti(cfg)
        convert_csv_main(studenti)
        studenti_validi = validaz_csv_main()
        converter_cvs_json(studenti_validi)

    elif comando == "report":
        
        cfg = config()
    
        studenti_validi = validaz_csv_main()
        
        risultati, top_5 = elabora_studenti(studenti_validi)
      
        statistiche_materie = calcoli_statistiche(studenti_validi)
        print(f"DEBUG: statistiche_materie = {statistiche_materie}")
        salva_rep(cfg, studenti_validi, top_5, statistiche_materie)
        
    else:
        print("Comando non riconosciuto. Usa 'generate', 'validate', 'all' o 'report'.")

if __name__ == '__main__':
    main()
