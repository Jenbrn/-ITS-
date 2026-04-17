import sys

print(F"versione di python in uso: {sys.version}")
print(F"Argomenti passati allo script: {sys.argv}")

# if len(sys.argv) != 3:
#     print("Uso: python script.py nome eta")
#     sys.exit(1)

# nome = sys.argv[1]
# eta = int(sys.argv[2])

# print(nome, eta)

x = [1,2,3]
print(sys.getsizeof(x))