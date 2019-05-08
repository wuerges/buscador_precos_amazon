import pandas as pd
import sys
import procurar
import pickle


def price(f, ref):
    pr = precos.get(ref)
    if pr:
        return f(pr)
    else:
        return 10000

def avg(xs):
    return sum(xs) / len(xs)

with open(sys.argv[1], "rb") as f:
    precos = pickle.load(f)

for arg in sys.argv[2:]:
    sheet = pd.read_csv(arg)
    sheet["min_price"] = sheet["REFERENCIA_ORDENADA"].apply(lambda x: price(min, x))
    sheet["max_price"] = sheet["REFERENCIA_ORDENADA"].apply(lambda x: price(max, x))
    sheet["avg_price"] = sheet["REFERENCIA_ORDENADA"].apply(lambda x: price(avg, x))
    print(sheet)
        # sheet["max_price"] = max(pr)
        # sheet["avg_price"] = sum(pr) / len(pr)
