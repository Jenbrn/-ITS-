""" Liste """

frutti = ['mele', 'pere', 'banane', 'mandarini']

for frutto in frutti:
    print(f"il frutto corrente è: {frutto} ed è di tipo {type(frutto)}")

for i in range(len(frutti)):
    print(f"Il frutto corrente è: {frutti[i]} ed è di tipo {type(frutti[i])}")

for i in range(len(frutti)):
    print(f"Il {i+1}° frutto è: {frutto} ed è di tipo {type(frutti)}")

for x in enumerate(frutti):
    print(f"Il valore di x è {x} ed è di tipo {type(x)}")