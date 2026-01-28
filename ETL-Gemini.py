from google import genai
from google.genai import types
import pandas as pd
import time
import os  # Importante para verificar se o arquivo existe

# --- CONFIGURAÇÃO da chave da api---
API_KEY = " " 
client = genai.Client(api_key=API_KEY)

ARQUIVO_ENTRADA = 'clientes_vips.csv'
ARQUIVO_SAIDA = 'clientes_processados_checkpoint.csv' # Arquivo que vai salvando aos poucos

# ============================================================
# ETAPA 1: EXTRACT (INTELIGENTE)
# ============================================================
print("1. Lendo arquivos...")

# 1.1 Lê a lista original
try:
    df_todos = pd.read_csv(ARQUIVO_ENTRADA)
except FileNotFoundError:
    print(f"Erro: O arquivo '{ARQUIVO_ENTRADA}' não existe.")
    exit()

# 1.2 Verifica se já existe trabalho salvo para continuar de onde parou
ids_processados = []
if os.path.exists(ARQUIVO_SAIDA):
    df_salvos = pd.read_csv(ARQUIVO_SAIDA)
    ids_processados = df_salvos['id'].tolist()
    print(f"🔄 Encontrei {len(ids_processados)} clientes já processados! Pulando eles...")

# 1.3 Filtra o DataFrame para pegar APENAS quem ainda não foi processado
# (O símbolo ~ significa "NÃO", ou seja: pegue onde o ID NÃO está na lista de processados)
df_para_processar = df_todos[~df_todos['id'].isin(ids_processados)]

total_restante = len(df_para_processar)
print(f"🎯 Restam {total_restante} clientes para processar.")

if total_restante == 0:
    print("✅ Todos os clientes já foram processados! Nada a fazer.")
    exit()

# ============================================================
# ETAPA 2: TRANSFORM & LOAD (AO MESMO TEMPO)
# ============================================================
print("2. Iniciando processamento com Salvamento Automático...")

def gerar_texto(nome, interesse):
    prompt = (
    f"Aja como um consultor financeiro. Crie um slogan de 1 frase para {nome} sobre {interesse}. "
    "Foco em benefícios. Máximo 12 palavras."
)
    
    tentativas = 0
    while tentativas < 3:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite", 
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            if "429" in str(e) or "RESOURCE" in str(e):
                print(f"✋ Rate Limit em {nome}. Esperando 60s...")
                time.sleep(60)
                tentativas += 1
            else:
                print(f"❌ Erro em {nome}: {e}")
                return "Erro técnico"
            
    return "Falha após tentativas"

# Loop linha a linha (Em vez de apply, usamos for loop para salvar na hora)
for index, linha in df_para_processar.iterrows():
    
    # 1. Processa a IA
    resultado_ia = gerar_texto(linha['nome'], linha['interesse'])
    
    print(f"✅ Feito: {linha['nome']}")
    
    # 2. Cria um mini-dataframe só com essa linha pronta
    # Copiamos a linha original e adicionamos a resposta
    df_linha_pronta = pd.DataFrame([linha])
    df_linha_pronta['marketing_ia'] = resultado_ia
    
    # 3. SALVA IMEDIATAMENTE NO DISCO (Mode 'a' = Append/Adicionar)
    # Se o arquivo não existe, escreve o cabeçalho. Se existe, não escreve.
    escrever_cabecalho = not os.path.exists(ARQUIVO_SAIDA)
    
    df_linha_pronta.to_csv(ARQUIVO_SAIDA, mode='a', index=False, header=escrever_cabecalho)
    
    # Pausa para evitar bloqueio do Google
    time.sleep(1)

print("Processo concluído! Todos os dados estão seguros em:", ARQUIVO_SAIDA)