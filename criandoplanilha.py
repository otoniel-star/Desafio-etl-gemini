import pandas as pd
import random

# Listas para gerar dados aleatórios, mas realistas
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Rafaela", "Samuel", "Tatiana", "Vitor", "Yasmin"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Almeida", "Pereira", "Lima", "Gomes", "Costa", "Martins", "Araujo", "Barbosa", "Ribeiro"]
interesses = [
    "Tesouro Direto", 
    "Ações e Bolsa de Valores", 
    "Fundos Imobiliários (FIIs)", 
    "Criptomoedas", 
    "Previdência Privada", 
    "Seguro de Vida", 
    "Cartão de Crédito Black", 
    "Financiamento de Imóveis", 
    "Reserva de Emergência", 
    "Day Trade"
]

dados = []

# Gerando 1000 linhas
print("Gerando 1.000 clientes falsos...")
for i in range(1, 1001):
    nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    interesse_cliente = random.choice(interesses)
    
    dados.append({
        "id": i,
        "nome": nome_completo,
        "interesse": interesse_cliente
    })

# Criando o DataFrame e salvando
df = pd.DataFrame(dados)
df.to_csv("clientes_vips.csv", index=False)

print("✅ Sucesso! Arquivo 'clientes_vips.csv' criado com 1.000 linhas.")