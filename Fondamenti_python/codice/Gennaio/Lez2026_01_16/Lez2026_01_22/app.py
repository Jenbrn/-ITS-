saluto = 'HELLO virtual machine!'

print(saluto)

#metodi delle stringhe
print(saluto.capitalize())
print(saluto.upper())  
print(saluto.lower())

#lunghezza stringa
lunghezza = len(saluto)

print(lunghezza)

#print("questa stringa è lunga " + lunghezza + "caratteri") non posso usare + tra stringa e numero
print(type(lunghezza))#trasformo in str
str(lunghezza)#forzo il passaggio in num
temp = str(lunghezza)#assegno variab temp
print(type(temp))
print("questa stringa è lunga " + temp + " caratteri")
print(f"questa stringa è lunga {lunghezza} caratteri")
#{} altgr ctrl shift

# metodi delle stringhe
print(saluto.capitalize())
print(saluto.upper())
print(saluto.lower())

#lunghezza della string
lunghezza = len(saluto)

# print(type(lunghezza))

# temp = str(lunghezza)
# print(type(temp))

print(f"Questa stringa è lunga {lunghezza} caratteri")