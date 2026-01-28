import pandas as pd

# 1. Lê o arquivo CSV que parece "quebrado"
# O Pandas é inteligente e entende a vírgula sozinho
df = pd.read_csv('clientes_processados_checkpoint.csv')

# 2. (Opcional) Remove linhas que deram erro para limpar a planilha
# Se quiser manter os erros para ver, apague esta linha abaixo
df_limpo = df[df['marketing_ia'] != "Erro técnico"]

print(f"Recuperamos {len(df_limpo)} clientes processados com sucesso!")

# 3. Salva como Excel verdadeiro (.xlsx)
# index=False tira aquela coluna de numeração extra
df_limpo.to_excel("Relatorio_Final_Clientes.xlsx", index=False)

print("✅ Sucesso! Abra o arquivo 'Relatorio_Final_Clientes.xlsx'")