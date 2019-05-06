import pandas as pd
import sys

sheets = []

for arg in sys.argv[1:]:
    print(arg)
    sheet = pd.read_csv(arg)
    sheet["Curso"] = arg
    sheets.append(sheet)

sheets = pd.concat(sheets)
