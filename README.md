<div align="center">

# 🚀 Pipeline de ETL com IA Generativa
### Automação de Marketing com Google Gemini e Resiliência de Dados

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20AI-Gemini%20Flash-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

</div>

---

## 📋 O Desafio
O objetivo deste projeto foi construir um pipeline de **ETL (Extract, Transform, Load)** robusto, capaz de ler uma base de dados de clientes, utilizar Inteligência Artificial para gerar mensagens de marketing hiper-personalizadas e salvar os resultados de forma organizada, contornando limitações de APIs gratuitas.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
| :--- | :--- |
| **Python 3.12** | Linguagem principal |
| **Pandas** | Manipulação e leitura de dados tabulares |
| **Google GenAI SDK** | Integração com o modelo **Gemini 2.5 Flash Lite** |
| **Time & OS** | Controle de fluxo e manipulação de sistema de arquivos |

---

## 🛤️ A Jornada de Desenvolvimento

### 🔄 Fluxo de Processamento (Pipeline)
```mermaid
graph TD;
    A[📂 CSV Bruto] -->|Leitura| B(🐍 Script Python);
    B --> C{🔍 Já processado?};
    C -->|Sim| B;
    C -->|Não| D[🤖 API Gemini];
    D -->|❌ Erro 429| E[💤 Dormir 60s];
    E --> D;
    D -->|✅ Sucesso| F[💾 Salvar Checkpoint];
    F -->|Fim do Loop| G[📊 Exportar Excel (.xlsx)];
📍 Fase 1: Fundamentação (Extract)
Entendemos a necessidade de lidar com dados tabulares.

Ação: Criação do gerador_dados.py simulando 1.000 clientes com interesses em Cripto, FIIs e Ações.

🚧 Fase 2: Obstáculos Iniciais
Tentamos uma abordagem clássica com pandas.apply(), mas encontramos barreiras:

🛑 Problema 1: Depreciação da SDK antiga (google.generativeai). ✅ Solução: Migração para a nova SDK google.genai.

🛑 Problema 2: Rate Limiting (Erro 429) e perda de dados em memória. ✅ Solução: O script quebrava ao processar 1.000 linhas de uma vez.

⚙️ Fase 3: Engenharia e Resiliência (Transform)
Tornamos o script "À prova de falhas":

Lógica de Retry (Backoff): Loop while que identifica o Resource Exhausted. Se der erro, o script dorme por 60s e tenta novamente.

Persistência (Checkpoint): Salvamento linha a linha (mode='a') no disco. Nada é perdido se a luz acabar.

Filtro Inteligente (Delta Load): Verifica IDs já processados para permitir "pausar e continuar".

Engenharia de Prompt: Limitação para "Máximo 12 palavras", economizando tokens e acelerando a API.

📦 Fase 4: Carregamento (Load)
Houve conflito de separadores (, vs ;) no Excel brasileiro.

Solução: Script final converter do CSV bruto processado para Excel nativo (.xlsx).

🏆 Resultados Alcançados
[x] Pipeline 100% automatizado e resiliente.

[x] Processamento de grandes volumes respeitando o Free Tier.

[x] Custo Zero de infraestrutura.

[x] Mensagens de marketing altamente personalizadas geradas.

<div align="center"> <sub>Projeto desenvolvido para fins de estudo em Engenharia de Dados e IA.</sub> </div>

