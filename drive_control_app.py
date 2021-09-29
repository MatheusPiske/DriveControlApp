# Importações e análise de dados

import pandas as pd

with open('usuarios.txt', 'r') as f:
    results = [[entry for entry in line.split()] for line in f.readlines()]

# Loops para manipulação dos dados

lista_nomes = []
for nomes in results:
  lista_nomes.append(nomes[0])
  
lista_dados = []
for dados in results:
    lista_dados.append(int(dados[1]))   

bytes_megabytes = []
for i in lista_dados:
    bytes = round(i*0.0000009536743, 2)
    bytes_megabytes.append(bytes)

porcentagem_ocupada = []
for i in bytes_megabytes:
    espaco_total = sum(bytes_megabytes)
    porcentagem = round(espaco_total / 100, 2)
    porcentagem = round(i/porcentagem, 2)
    porcentagem_ocupada.append(str(porcentagem) + '%')

# Resultados finais

espaco_total = sum(bytes_megabytes)
quantidade_usuarios = len(lista_nomes)
espaco_medio = espaco_total / quantidade_usuarios

# Estruturação da planilha ()

dados_usuarios = {'     Usuário' : lista_nomes, '     Espaço Utilizado em MB' : bytes_megabytes, '     % do uso' : porcentagem_ocupada}

print('ACME Inc.                         Uso do espaço em disco pelos usuários')
print('-----------------------------------------------------------------------')
print('-----------------------------------------------------------------------')

# DataFrame criado com os dados 

dados_usuariosDF = pd.DataFrame(dados_usuarios)
print(dados_usuariosDF)

# ()

print('\nEspaço total ocupado: ' + str(round(espaco_total, 2)) + ' MB')
print('Espaço médio ocupado: ' + str(round(espaco_medio, 2)) + ' MB')

input()



