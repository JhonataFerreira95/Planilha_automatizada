from openpyxl import load_workbook

wb = load_workbook("data/pivot_table.xlsx")
sheet = wb["Relatorio"]

print(sheet["A3"].value)
print(sheet["B3"].value)

for i in range(2, 6):
    ano = sheet["A%s" %i].value
    am = sheet["B%s" %i].value
    bt = sheet["C%s" %i].value
    jg = sheet["D%s" %i].value
    mg = sheet["E%s" %i].value
    rr = sheet["F%s" %i].value
    print("{0} o Aston martin vendeu {1} e o Bentley vendeu {2}, jaguar vendeu {3}, MGB vendeu {4}, Rolls Royce vendeu {5}".format(ano, am, bt, jg, mg, rr))
