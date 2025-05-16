import re
from collections import Counter

#Abre arquivo no modo leitura
with open('/content/texto.txt', 'r', encoding='utf-8') as arquivo:
  conteudo=arquivo.read()

texto = re.sub(r'[^\w\s]', '', conteudo)

texto = texto.lower();

#dividi o texto em uma lista de palavras
palavras = texto.split()

#Dicionário para armazenar as contagens
contagem = {}

#Contar as palavras
for palavra in palavras:
  if palavra in contagem:
    contagem[palavra] += 1
  else:
    contagem[palavra] = 1

contador = Counter(contagem)

#salvando tudo em um arquivo
arquivo_dados='estatisticas.txt'
with open(arquivo_dados, 'w', encoding='utf-8') as arquivo_saida:
  arquivo_saida.write('=== PALAVRAS MAIS FREQUENTES ===\n')
  for palavra, frequencia in contador.most_common(10):
    arquivo_saida.write(f'{palavra}: {frequencia}\n')

print(f"Dados salvos em '{arquivo_dados}'!")
