from datetime import date, datetime, timedelta

oggi = date.today()

print(oggi)
print(oggi.year)
print(oggi.month)
print(oggi.day)
adesso = datetime.now()
print(adesso)
print(adesso.year, adesso.month, adesso.day)
print(adesso)

fra_20_min = adesso + timedelta(minutes=20)
# print(F"l'intervallo termina alle h : {fra_20_min}")
print(adesso.strftime("%d/%m%Y"))