# -*- coding: utf-8 -*-
"""
# Exercicio 1

A proposta do exercício é coletar os dados dos sorteios da Lotofácil disponibilizados pela CEF e responder as seguintes perguntas:
- Qual o número mais sorteado e o menos sorteado?
- Quais combinações de números Pares(p), Impares(i) e Primos(np) saem por sorteio?
"""

# Importar as bibliotecas necessárias
import requests
import pandas as pd
import collections

# armazenar a url dos resultados em uma variável 
url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/!ut/p/a1/jc4xD4IwEAXgn9QHpQXGQg1QUXBAoYtpojFNLDoYB3-91ZgYB9G76ZLv5R7RpCd6NFd7MBd7Gs3xcWu-5UGNEgVUoyoGMW8o7eQ6QMI8GDzIC1FGcQ0gSkJUMitlnC6Aiv-Xx5cR-JXfEP1Jijb3pJFZCuoX7AWmKj7BRIfBl4zfL5KlmkGELAyUoBQrTjpnR-vsbb8jZ9f1sK27A6NCXAk!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K85260Q5OIRSC42046/res/id=historicoHTML/c=cacheLevelPage/=/'

# utilizando a função get da biblioteca requests armazenar os dados da url em uma outra variável
data = requests.get(url)

# usando a função read_html da biblioteca pandas armazenar os dados em formato html em uma nova variável
dataframe = pd.read_html(data.text)

# para retornar os dados em um data frame formatado vamos realizar a cópia dos dados dentro da mesma variável
dataframe=dataframe[0].copy()

#vamos chamar a veriavél para verificar como estão sendo retornados os dados
# dataframe

# a Lotofácil tem uma população de 25 números e desses o apostador escolhe 15, 
# para continuarmos vamos criar a população dos 25 números usando uma lista preenchida utilizando range
nr_pop = list(range(1,26))
# Agora vamos definir os grupos dos Pares(p), Impares(i) e Primos(np) os quais devemos informar cada número
nr_pares = [2, 4, 6, 8, 10 ,12, 14, 16, 18, 20, 22, 24]
nr_impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
nr_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]

# Vamos agora criar variaveis para cada combinação començando pela variavel que irá armazenar as combinações
# de pares, impares e primos como uma lista
comb = []

# agora criaremos 25 variaveis para armazernar a quantidade de vezes que um determinado número aparece
v_01 = 0
v_02 = 0
v_03 = 0
v_04 = 0
v_05 = 0
v_06 = 0
v_07 = 0
v_08 = 0
v_09 = 0
v_10 = 0
v_11 = 0
v_12 = 0
v_13 = 0
v_14 = 0
v_15 = 0
v_16 = 0
v_17 = 0
v_18 = 0
v_19 = 0
v_20 = 0
v_21 = 0
v_22 = 0
v_23 = 0
v_24 = 0
v_25 = 0

# preciso definir quais variaveis iremos interar no Data Frame vemos que os numeros sorteados são chamados de 
# bola 1, bola, 2, etc.. sendo assim vamos criar uma lista com os nomes desses campos

lst_campos = ['Bola1','Bola2','Bola3','Bola4','Bola5',
              'Bola6','Bola7','Bola8','Bola9','Bola10',
              'Bola11','Bola12','Bola13','Bola14','Bola15']

# Agora vamos realizar a iteração percorrendo o DF usando a função iterrows() e preenchendo as variaveis 
# v_pares, v_impares e v_primos que iremos inicializar com valor 0
 
for index,row in dataframe.iterrows():
  v_pares=0
  v_impares=0
  v_primos=0
  for campo in lst_campos:
    if row[campo] in nr_pares:
      v_pares += 1
    if row[campo] in nr_impares:
      v_impares += 1
    if row[campo] in nr_primos:
      v_primos += 1
    if row[campo] == 1:
      v_01 += 1
    if row[campo] == 2:
      v_02 += 1
    if row[campo] == 3:
      v_03 += 1
    if row[campo] == 4:
      v_04 += 1
    if row[campo] == 5:
      v_05 += 1
    if row[campo] == 6:
      v_06 += 1
    if row[campo] == 7:
      v_07 += 1
    if row[campo] == 8:
      v_08 += 1
    if row[campo] == 9:
      v_09 += 1
    if row[campo] == 10:
      v_10 += 1
    if row[campo] == 11:
      v_11 += 1
    if row[campo] == 12:
      v_12 += 1
    if row[campo] == 13:
      v_13 += 1
    if row[campo] == 14:
      v_14 += 1
    if row[campo] == 15:
      v_15 += 1
    if row[campo] == 16:
      v_16 += 1
    if row[campo] == 17:
      v_17 += 1
    if row[campo] == 18:
      v_18 += 1
    if row[campo] == 19:
      v_19 += 1
    if row[campo] == 20:
      v_20 += 1
    if row[campo] == 21:
      v_21 += 1
    if row[campo] == 22:
      v_22 += 1
    if row[campo] == 23:
      v_23 += 1
    if row[campo] == 24:
      v_24 += 1
    if row[campo] == 25:
      v_25 += 1
  comb.append(str(v_pares) + 'p-' + str(v_impares) + 'i-' + str(v_primos) + 'np')

# Agora vamos dar uma olhada na variável comb, podemos perceber que ela armazenou a combinação de numeros
# pares, impares e primos em uma string
# comb

# agora vamos criar uma lista para armazenar a frequência que os numeros foram sorteados
freq_nr = [
           [1, v_01],
           [2, v_02],
           [3, v_03],
           [4, v_04],
           [5, v_05],
           [6, v_06],
           [7, v_07],
           [8, v_08],
           [9, v_09],
           [10, v_10],
           [11, v_11],
           [12, v_12],
           [13, v_13],
           [14, v_14],
           [15, v_15],
           [16, v_16],
           [17, v_17],
           [18, v_18],
           [19, v_19],
           [20, v_20],
           [21, v_21],
           [22, v_22],
           [23, v_23],
           [24, v_24],
           [25, v_25]
           ]
# e agora vamos ordenar a lista do que menos saiu para o que mais saiu usando a função sort
freq_nr.sort(key=lambda tup: tup[1])

# vamos dar uma olhada nos resultados
# freq_nr

# agora já podemos responder qual foi o número menos sorteado e o mais sorteado buscando o primeiro e o ultimo
menos_freq = freq_nr[0] 
mais_freq = freq_nr[-1]

counter = collections.Counter(comb)
resultado=pd.DataFrame(counter.items(),columns=['Combinacao','Frequencia'])
resultado['p_freq'] = resultado['Frequencia']/resultado['Frequencia'].sum()
resultado = resultado.sort_values(by='p_freq')

# agora vamos mostrar o resultado final de uma forma amigavel

print('''
O número que mais foi sorteado foi o número: {}
O número que menos foi sorteado foi o número: {}
Acombinação de Pares(p), Impares(i) e Primos(np) mais frequente é :{} com uma frequencia de: {}%
'''
.format(mais_freq[0],menos_freq[0],resultado['Combinacao'].values[-1],round(resultado['p_freq'].values[-1]*100,2))
)
