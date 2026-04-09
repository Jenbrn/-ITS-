import requests

# url = 'https://pokeapi.co/api/v2/pokemon/'

# #risposta = requests.get( url + 'pikatcu')
# risposta = requests.get( url + 'pichu')

# if risposta.status_code == 200:
#     pokemon =risposta.json()
    
    
    
#     for chiave, valore in pokemon.items():
#         print(F" chiave: {chiave} valore. {valore}")
#         print('---------------------')




#print(risposta.status_code)

url = "https://api.tvmaze.com/singlesearch/shows?q="

cerca = input('Scrivi titolo: ')

risposta = requests.get(url + cerca)

if risposta.status_code == 200:
    show = risposta.json()

    titolo = show.get('name')
    rating = show.get('rating')
    image = show.get('image')

    print(titolo, rating['average'], image['medium'])