import pandas as pd
import sys
import procurar

sheets = []

for arg in sys.argv[1:]:
    sheet = pd.read_csv(arg)
    sheet["Curso"] = arg
    sheets.append(sheet)

sheets = pd.concat(sheets)
books = sheets["REFERENCIA_ORDENADA"]
groups = books.groupby(books).count().to_frame(name='contagem').reset_index()
groups = groups.sort_values(by='contagem')


crawler = procurar.Crawler()

print(groups)

precos = {}

for index, book in groups.iterrows():
    ref = book["REFERENCIA_ORDENADA"]
    print(ref, book)
    precos = crawler.procura(ref)
