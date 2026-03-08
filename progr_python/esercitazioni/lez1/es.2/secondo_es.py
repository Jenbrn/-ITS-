"""
    Autore: Janice Brun
    Data: 08/03/2026
    Titolo: Testo esercizio
    Si hanno in input N saldi di conti correnti bancari. Si vuole in output la media aritmetica dei
    soli conti correnti che hanno un saldo negativo."""

# Sezione di input Dati

lista_cc = []

lista_negativi = []


# Inizializzazioni variabili

while True:
    dato_grz = input('Inserisci il saldo del tuo Conto corrente (Premi q per uscire): ').lower()
    if dato_grz == 'q':
        print('Sessione terminata.')
        break
    try:
        saldo = float(dato_grz)
        lista_cc.append(saldo)
        if saldo < 0:
            lista_negativi.append(saldo)
    except ValueError:
        print('Valore non valido, inserire saldo CC o q per uscire.')


# Elaborazione

def c_media(a,b):
   return(a / b)

if len(lista_negativi) > 0:
    media_saldi_negativi = c_media(sum(lista_negativi), len(lista_negativi))

# Eventuali sotto processi di Elaborazione

# Sezione di output

print(f'Sono stati inseriti {len(lista_cc)} saldi di cui {len(lista_negativi)} sono in negativo.')
print(f'La media dei saldi in negativo è di: {media_saldi_negativi}€')