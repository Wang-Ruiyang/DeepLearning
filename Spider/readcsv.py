import pandas as pd

df = pd.read_csv("army.csv",header=None)
print(len(df.values))

datalist = df.values.tolist()

for i in range(len(datalist)):
    print(datalist[i])

# for i in data:
#     print(i)
#     print()