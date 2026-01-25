#Importando pandas
import pandas as pd

#importa biblioteca de ia do gemini
import google.generativeai as google_IA

#importa tempo de espera para evitar cair durante as requisições
import time
#import os

#configurando
API_KEY = input("SUA CHAVE: ")

#configurando a chave na biblioteca
google_IA.configure(api_key=API_KEY)

#escolhe o modelo
model = google_IA.GenerativeModel('gemini-pro')


#----- extraindo/ lendo o arquivo

