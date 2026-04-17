import os

# os.chdir("../")

print(F"Directoruy corrente: {os.getcwd()}")
print(F"Contenuto directory: {os.listdir('.')}")

# studenti_file = open("studenti.txt", "r", encoding="utf-8", newline='\n')
# lettura = studenti_file.read()
# for riga in lettura.splitlines():
#     os.mkdir(riga.strip())

# studenti_file.close()


# os.mkdir("fatta_in_fad")
#  os.mkdir("a/b/c")
# os.rmdir("fatta_in_fad")
for elem in os.listdir('.'):
    print(elem)

