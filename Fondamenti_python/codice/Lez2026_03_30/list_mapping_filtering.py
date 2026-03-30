"""liste-mapping-lambda"""
voti = [25,28,24,27,29,30,18,25]

# voti_plus = []

# for voto in voti:
#     voto += 1
#     voti_plus.append(voto)


def incrementa_voto(v):
    return v + 1

#voti_plus = list(map(incrementa_voto,voti))

voti_plus = list(map(lambda v:v + 1, voti))

print(voti_plus)

"""list compre"""

voti = [v+1 for v in voti]
#si parte a scrivere dal ciclo e poi aggingi davanti v+1 cioè quello che vuoi ottenere

"""FILTER LAMBDA VS LIST CMP"""

voti_plus_plis = list(filter(lambda v : v > 24,  voti) )

voti_plus_plis = [v for v in voti if v > 24]

print(voti_plus_plis)

