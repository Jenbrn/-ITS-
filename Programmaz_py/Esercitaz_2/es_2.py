"""
Autore: Janice Brun
Data: 25/03/2026
Titolo: Secondo Esercizio
    Creare una funzione che abbia come parametri formali un numero arbitrario di valori
    numerici. Si vuole che restituisca la somma dei soli numeri pari e il prodotto dei soli numeri
    dispari. Successivamente creare un programma che richiami tale funzione e che stampi in
    output i risultati . No standard input.
    """

def pari_dispari(*numero: int):
    """Funzione: Utilizzo un ciclo for per scorrere i numeri, se il resto della divisione è
       0 significa che è pari quindi partendo da un contatore 0 gli sommo tutti i pari. 
       stesso procedimento per i dispari ma moltiplicandoli partendo da base 1

       Parametri : sequenza arbitraria di valori numerici interi

       Return : restituisce 2 valori interi, uno associato alla somma 
       dei numeri pari e uno al prodotto dei dispari    
    """
    somma_pari = 0
    prod_dispari = 1
    for num in numero:
        if num % 2 == 0:
            somma_pari += num
        else:
            prod_dispari *= num
    return somma_pari, prod_dispari


def main():
    """Funzione : esegue la funzione pari_dispari su un tot di numeri inseriti 
       associa i due valori risultanti dalla funzione a due vairabili ( pari - disp)
       Li stampa .

       return: stampa i risultati della funzione pari_dispari  
    """
    pari, disp = pari_dispari(1,0,3,4,5,6)
    print(f"dati i numeri (1,2,3,4,5,6) la somma di tutti i numeri pari sarà = {pari} e il prodotto di tutti i numeri dispari = {disp}")


if __name__ == '__main__':
    main()

#alternativa per avere fstring finamica e non dover correggere cod in caso si volessero mod inumeri ma crea una tupla 
# def main():
#     valori = 1,2,3,4,5,6
#     pari, disp = pari_dispari(*valori)
#     print(f"dati i numeri {valori} la somma di tutti i numeri pari sarà = {pari} e il prodotto di tutti i numeri dispari = {disp}")



#while pari_dispari = 0: