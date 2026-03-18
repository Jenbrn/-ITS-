#Immagine python ufficiale leggera
FROM python:3.11-slim

# Imposto la dir di lavoro interna al container
#Tutti i prossimi comandi saranno eseguiti dentro /app
WORKDIR /app

# copia solo req.txt nella dir di lavoro
#se req.txt non cambia posso cachare
COPY requirements.txt .

#Installo dipendenze python senza salvare cache
#--no-cache-dir <- Immagine più leggera
RUN pip install --no-cache-dir -r requirements.txt

# prendi e copia tutto il resto del progetto (file .py, cartelle, ecc.)
#nella dir /app del container
COPY . .

# Dichiaro porta da esporre
EXPOSE 5000

# CMD -> comando avvio container
# Avvia app.py usando Python
CMD ["python", "app.py"]