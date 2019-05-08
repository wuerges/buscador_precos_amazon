import pickle, sys

with open(sys.argv[1], "rb") as f:
    precos = pickle.load(f)

for k, v in precos.items():
    print(k, v)
