import pandas as pd

data = pd.read_excel("data/VendaCarros.xlsx")


#DataFrame

df = data[["Fabricante", "ValorVenda", "Ano"]]


pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_table)

pivot_table.to_excel("data/pivot_table.xlsx", "Relatorio")
