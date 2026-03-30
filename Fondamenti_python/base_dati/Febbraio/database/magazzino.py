
magazzino = [
    ['maglia gialla', 100],
    ['maglia rossa', 50],
    ['maglia verde', 70],
    ['maglia blu', 150]
]

f = open('magazzino.html', 'w')

f.write('<html>\n')
f.write('<head>\n')
f.write('<head>\n')
f.write('<body>\n')

f.write('<h1>Magazzino prodotti</h1>\n')

f.write('<ul>\n')

for prodotto in magazzino:
    nome = prodotto[0]
    quantità = prodotto[1]
    
    f.write(f"<li>{nome}:{quantità}<li>")

f.write('<ul>\n')

f.write('<body>\n')
f.write('<html>\n')

f.close()
print('elaborazione terminata')