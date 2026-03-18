import pandas as pd

df = pd.read_csv("ezerML.csv")
print(df.to_numpy())
df["color"] = df["color"].astype("category").cat.codes
df["quality"] = df["quality"].astype("category").cat.codes
#i chose to encode the color&quality columns (for example red->1 , blue ->2 ...) 

print(df.to_numpy())
