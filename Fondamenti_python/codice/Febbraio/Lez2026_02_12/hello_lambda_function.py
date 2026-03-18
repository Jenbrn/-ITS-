'''LAMBDA FUNCTION'''

voti = [15, 25, 18, 28, 26, 30, 24, 28]

voti_24_plus = [ x for x in voti if x > 24 ] #list comprehansion

voti_24_lambda = list(map(lambda x : x - 2, voti))

print(voti_24_lambda)
print(voti_24_plus)
