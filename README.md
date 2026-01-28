🚀 Relatório de Projeto: Pipeline de ETL com IA Generativa
1. O Desafio
O objetivo deste projeto foi construir um pipeline de ETL (Extract, Transform, Load) capaz de ler uma base de dados de clientes, utilizar Inteligência Artificial o chat gpt mas eu preferi optar pelo (Google Gemini) para gerar mensagens de marketing personalizadas para cada um e salvar o resultado de forma organizada.

2. Tecnologias Utilizadas
Linguagem: Python 3.12

Manipulação de Dados: Pandas

Inteligência Artificial: Google GenAI SDK (Gemini 2.5 Flash Lite)

Controle de Fluxo: Time & OS (Bibliotecas padrão)

3. A Jornada de Desenvolvimento
Fase 1: Fundamentação e Extração (Extract)
Inicialmente, exploramos a diferença entre bancos relacionais (SQL) e não-relacionais (NoSQL), entendendo que para este projeto, lidaríamos com dados tabulares (CSV).

Ação: Criamos um script gerador de dados (gerador_dados.py) que simulou uma base de 1.000 clientes com nomes e interesses financeiros variados (Cripto, FIIs, Ações).

Fase 2: Primeira Implementação e Obstáculos
Na primeira versão do ETL, utilizamos a abordagem clássica com pandas.apply() para processar a IA linha a linha. Enfrentamos três problemas críticos:

Depreciação de SDK: A biblioteca google.generativeai entrou em modo de manutenção.

Solução: Migramos para a nova SDK google.genai, garantindo longevidade ao código.

Rate Limiting (Erro 429): O plano gratuito do Google bloqueou as requisições por excesso de velocidade ao tentar processar 1.000 linhas de uma vez.

Perda de Dados em Memória: Ao interromper o script (ou em caso de falha), todo o progresso era perdido, pois o salvamento ocorria apenas no final.

Fase 3: Engenharia e Resiliência (Transform)
Para tornar o script robusto ("A prova de falhas"), implementamos soluções de Engenharia de Dados avançadas:

Lógica de Retry (Backoff): Criamos um loop while que identifica o erro 429 (Resource Exhausted). Quando detectado, o script "dorme" por 60 segundos e tenta novamente, sem quebrar a execução.

Persistência de Estado (Checkpoint): Substituímos o processamento em memória por um loop for que salva no disco rígido (mode='a') a cada linha processada.

Filtro Inteligente: O script verifica quais IDs já foram salvos no CSV de saída e processa apenas o que falta (Delta Load). Isso permite parar e continuar o script a qualquer momento.

Engenharia de Prompt: Refinamos o prompt para solicitar respostas de "Máximo 12 palavras". Isso economizou tokens e acelerou o tempo de resposta da API.

Fase 4: Carregamento e Apresentação (Load)
O arquivo final gerado (.csv) apresentou problemas de formatação ao abrir no Excel brasileiro (conflito de separadores , vs ;).

Solução: Criamos um script final de conversão que lê o CSV bruto processado e exporta para um arquivo Excel nativo (.xlsx), pronto para ser entregue ao time de negócios.

4. Resultados Alcançados
✅ Pipeline 100% automatizado e resiliente a falhas de rede/API. ✅ Capacidade de processar grandes volumes de dados respeitando limites do Free Tier. ✅ Custo zero de infraestrutura (rodando localmente com API gratuita). ✅ Geração de mensagens de marketing altamente personalizadas.
