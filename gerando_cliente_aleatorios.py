#app que gera uma tabela aleatoria para uso de ETL posteriormente
import pandas as pd #Importa a biblioteca pandas e apelida de pd
import random #Importa biblioteca de sorteio

#Dados que serao usados

#Lista de nomes
nome = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel"]

#Lista de Sobrenomes 
sobrenome= ["Silva","Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira"]

#Listas de interesse financeiros
interesse = [
    "tesouro direto",
    "Ações",
    "Fundos Imobiliarios",
    "Criptomoedas",
    "Reserva de Emergencia"
]

#Lista vazia para os clientes gerados
Clientes_Gerados = []

print("Gerando clientes fictcios...")

#loop que roda 50 vezes 
#O 'range(1,5)' gera um  numero de 1 ate 50

for i in range (1,50):
    #Sorteia um nome e um sobrenome e coloca um espaço no meio
    nome_completo = f"{random.choice(nome)} {random.choice(sobrenome)}"

    #Sorteia um interesse da lista
    interesse_cliente = random.choice (interesse)

    #Adciona um dicionario (par chave: valor) na nossa lista dados
    Clientes_Gerados.append({
        "id": i,
        "nome":nome_completo,
        "interesse": interesse_cliente
    })

    #------Salvando------

    #transformando a lista de dicionario em um dataframe(tabela do pandas)
    df = pd.DataFrame(Clientes_Gerados)

    #Salvando em um arquivo csv
    df.to_csv("Clientes_gerados.csv", index = False)
print("😊 clientes gerados!!!!")

