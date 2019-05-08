import pandas as pd
import sys
import procurar
import pickle

sheets = []

precos = {}
try:
    with open(sys.argv[1], "rb") as f:
        precos = pickle.load(f)
except:
    print("Failed to load pickle, creating a new dict")

for arg in sys.argv[2:]:
    sheet = pd.read_csv(arg)
    sheet["Curso"] = arg
    sheets.append(sheet)

sheets = pd.concat(sheets)
books = sheets["REFERENCIA_ORDENADA"]
groups = books.groupby(books).count().to_frame(name='contagem').reset_index()
groups = groups.sort_values(by='contagem')


crawler = procurar.Crawler()

for index, book in groups.iterrows():
    ref = book["REFERENCIA_ORDENADA"]
    if not ref in precos:
        print("adicionando", ref)
        pi = crawler.procura(ref)
        precos[ref] = pi
    else:
        print("pulando", ref)

    with open(sys.argv[1], "wb") as f:
        pickle.dump(precos, f)
