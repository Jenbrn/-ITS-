
""" Funzioni nel pitone """


# def presentazione(nome, cognome, hobby):
#     print(f'Benvenuto {nome} {cognome}, sono felice che il tuo hobby sia {hobby} ')

# presentazione('janice', 'brun', 'fotografia')
  
def presentazione(nome, hobby = 'fotografia', cognome = 'brun'):
    print(f'Benvenuta {nome} {cognome}, sono felice che il tuo hobby sia {hobby}.')

presentazione(hobby= 'fotografia', cognome= 'brun', nome= 'janice')