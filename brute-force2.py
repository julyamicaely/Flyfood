def ler_arquivo_matriz(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        return arquivo.read()

def formular_matriz(conteudo_matriz):
    linhas = conteudo_matriz.strip().split("\n")
    n_linhas, n_colunas = map(int, linhas[0].split())
    matriz = []
    for i in range(1, n_linhas + 1):
        valores = linhas[i].split()
        matriz.append(valores)
    return matriz

def encontrar_pontos(matriz):  # encontrar pontos de interesse
    loc_pontos = {}
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            valor = matriz[i][j]
            if valor != '0':
                loc_pontos[valor] = (i, j)
    return loc_pontos

def pontos_str(loc_pontos):
    juntar = []
    for i in loc_pontos:
        if i != 'R':
            juntar.append(i)
    return ''.join(juntar)

def permutacoes(pontos):
    if len(pontos) == 0:
        return ['']
    resultado = []
    for c in pontos:
        restante = pontos.replace(c, '')
        for p in permutacoes(restante):
            resultado.append(c + p)
    return resultado

def dist_manhattan(tupleA, tupleB):
    dist = abs(tupleA[0] - tupleB[0]) + abs(tupleA[1] - tupleB[1])
    return dist

def calcular_distancias(loc_pontos, rotas):  # calcular as distâncias do ponto de partida até os outros pontos
    distancias = []
    for rota in rotas:
        soma = 0
        for a, b in zip(rota, rota[1:]):
            soma += dist_manhattan(loc_pontos[a], loc_pontos[b])
        distancias.append((rota, soma))
    return distancias

def melhor_rota(distancia):
    menor_dist = distancia[0][1]
    melhor = distancia[0][0]
    for rota, dist in distancia[1:]:
        if dist < menor_dist:
            melhor, menor_dist = rota, dist
    return melhor, menor_dist

def retirar_rs(melhor_rota):
    return melhor_rota[1:-1]

import time

if __name__ == "__main__":
    conteudo = ler_arquivo_matriz("arquivo_1.txt")
    matriz = formular_matriz(conteudo)

    pontos = encontrar_pontos(matriz)
    ordem = pontos_str(pontos)
    rotas = ['R' + p + 'R' for p in permutacoes(ordem)]

    inicio = time.perf_counter()

    distancias = calcular_distancias(pontos, rotas)
    melhor_percurso, menor_dist = melhor_rota(distancias)

    fim = time.perf_counter()
    tempo_execucao = fim - inicio

    caminho = retirar_rs(melhor_percurso)

    print(f"Melhor percurso completo: {melhor_percurso}")
    print(f"Sequência interna sem Rs: {caminho}")
    print(f"Distância total: {menor_dist} drônometros!")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")