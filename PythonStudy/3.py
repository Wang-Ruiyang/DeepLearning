import pickle

with open("data.pkl","rb") as f:
    x, y, z, s, l, d = pickle.load(f)

print(x, y, z, s, l, d, sep="\n")
