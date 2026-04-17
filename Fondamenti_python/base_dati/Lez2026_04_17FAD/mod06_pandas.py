import pandas as pd
import matplotlib 
dfauto = pd.read_csv("auto.csv")
df = pd.read_csv("moto.csv")

# print(df)
"""
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
df.describe()
print(df.describe())
print(df[["Modello", "Modello"]])
print(df.iloc[0:2, 0:2])
"""
moto_sopra_10k = (df[df["Prezzo (€)"] > 10000] [["Marca", "Modello", "Prezzo (€)"]])
moto_sopra_10k.sort_values(by="Prezzo (€)", ascending=False, inplace=True)
moto_sopra_10k["IVA"] = 0.22
moto_sopra_10k["Valore_IVA"] = moto_sopra_10k["Prezzo (€)"] * moto_sopra_10k["IVA"]
# print(moto_sopra_10k)

# veioli = pd.concat([df, dfauto])
# print(veioli)

# veioli.to_csv('veioli.csv', index=False)
# veioli.to_json('veioli.json', indent=4)
# veioli.to_html("veicoli.html")
# veioli.to_excel("veicoli.xlsx")

matplotlib.pyplot.show()

#??





