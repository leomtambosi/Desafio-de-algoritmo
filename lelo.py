#Desafio de algoritmo da senha

import re

def pontuacao_senha(senha):
    pontos = 0
    num = len(senha)
    
    #Contagem dos caracteres
    maiusculas = sum(1 for c in senha if c.isupper())
    minusculas = sum(1 for c in senha if c.islower())
    numeros = sum(1 for c in senha if c.isdigit())
    simbolos = sum(1 for c in senha if not c.isalnum())
    
    #Pontuação positiva
    pontos += (num - maiusculas) * 2
    pontos += (num - minusculas) * 2
    pontos += numeros * 4
    pontos += num * 4
    pontos += simbolos * 6
    pontos += sum(1 for c in senha[1:-1] if c.isdigit() or not c.isalnum()) * 2
    
    #regra minimo de 8 digitos
    regras = 0
    if num >= 8:                                                               
        regras += 1

    #regra 3/4
    if (maiusculas >= 3/4 * num or minusculas >=3/4 * num or                       
        numeros >= 3/4 * num or simbolos >= 3/4 * num):                              
        regras += 1                                                                         
    pontos += regras * 2
    
    #Dedução
    if numeros == 0 and simbolos == 0:
        pontos -= num
    if maiusculas == 0 and minusculas == 0 and simbolos == 0:
        pontos -= numeros
    
    #Repetição
    repetidos = sum(1 for c in senha if senha.count(c) > 1)
    pontos -= repetidos
    
    #Dedução por repetição consecutiva
    for condicao, peso in [(str.isupper, 2), (str.islower, 2), (str.isdigit, 2)]:
        pontos -= sum(1 for i in range(1, len(senha)) if condicao(senha[i]) and condicao(senha[i-1]) and senha[i] == senha[i-1]) * peso
    
    #Dedução por sequências
    for padrao, peso in [(r"[a-zA-Z]{4,}", 3), (r"\d{4,}", 3), (r"[!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:'\",<>\./?\\|`~]{4,}", 3)]:
        pontos -= len(re.findall(padrao, senha)) * peso

    #Classificação
    if pontos < 10:
        classificacao = "Muito fraca"
    elif pontos < 30:
        classificacao = "Fraca"
    elif pontos < 50:
        classificacao = "Boa"
    elif pontos < 70:
        classificacao = "Forte"
    else:
        classificacao = "Muito Forte"
    return pontos, classificacao

senha = input("Digite sua senha: ")
pontuacao, classificacao = pontuacao_senha(senha)

print(f'Classificação: {classificacao}')
print(f'Pontos: {pontuacao}')
