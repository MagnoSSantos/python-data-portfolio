import pandas as pd

# 1) Ler o arquivo CSV
df = pd.read_csv("dados_brutos.csv")

# 2) Mostrar tamanho do dataset
print("Linhas e colunas:", df.shape)

# 3) Mostrar nomes das colunas
print("\nColunas:")
print(df.columns)

# 4) Criar nova coluna: valor por pessoa
df["valor_por_pessoa"] = (df["total_bill"] / df["size"]).round(2)

# 5) Agrupar dados por dia e calcular médias
resumo = df.groupby("day")[["total_bill", "tip"]].mean()

print("\nResumo médio por dia:")
print(resumo)

# 6) Salvar dados tratados
df.to_csv("dados_limpos.csv", index=False)

print("\nArquivo 'dados_limpos.csv' criado com sucesso!")

