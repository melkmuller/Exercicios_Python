# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

import requests
import json

#Resolvi pesquisar como pegar a cotação do dólar atual. Através de uma requisição que retorna um JSON, dele peguei a informação da cotação.
requisicao = requests.get(" https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic = requisicao.json()
dolarAgora = float(requisicao_dic["USDBRL"]['bid'])

dinheiro = float(input("Quanto dinheiro você tem agora na carteira? R$ "))
print(f'O Dólar está agora U$ {dolarAgora} ')
print(f'Com essa quantia você consegue comprar U$ {dinheiro/dolarAgora:.2f}')