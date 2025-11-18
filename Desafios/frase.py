import string
import math
import numpy as np

tabela = string.ascii_lowercase + ".!# "

def texto_para_lista(texto, tabela):
    return [tabela.index(c) + 1 for c in texto if c in tabela]

frase = "quem#exercita#aprende!"
chave = "azul"

lista_frase = texto_para_lista(frase, tabela)
lista_chave = texto_para_lista(chave, tabela)

n_linhas = 2
n_colunas = math.ceil(len(lista_frase) / n_linhas)

n_linhas_chave = 2
n_colunas_chave = math.ceil(len(lista_chave) / n_linhas_chave)

matriz_frase = [
    lista_frase[:n_colunas],
    lista_frase[n_colunas:]
]

matriz_chave = [
    lista_chave[:n_colunas_chave],
    lista_chave[n_colunas_chave:]
]

print("Matriz da frase:")
for linha in matriz_frase:
    print(linha)

print("\nMatriz da chave:")
for linha in matriz_chave:
    print(linha)

matriz_resultado = np.dot(matriz_chave, matriz_frase)
print("Matriz resultado:")
print(matriz_resultado)
