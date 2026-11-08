def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)

        for linha in matriz:
            linha.append(0)

        nova_linha = [0] * len(vertices)
        matriz.append(nova_linha)

        print("Vertice inserido com sucesso!")
    else:
        print("Vertice ja existe!")


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)

    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)

    if matriz[i][j] == 1:
        print("Aresta ja existe!")
        return

    matriz[i][j] = 1

    if nao_direcionado:
        matriz[j][i] = 1

    print("Aresta inserida com sucesso!")


def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        print("Vertice nao encontrado!")
        return

    indice = vertices.index(vertice)

    matriz.pop(indice)

    for linha in matriz:
        linha.pop(indice)

    vertices.pop(indice)

    print("Vertice removido com sucesso!")


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices or destino not in vertices:
        print("Vertice nao encontrado!")
        return

    i = vertices.index(origem)
    j = vertices.index(destino)

    if matriz[i][j] == 0:
        print("Aresta nao encontrada!")
        return

    matriz[i][j] = 0

    if nao_direcionado:
        matriz[j][i] = 0

    print("Aresta removida com sucesso!")


def existe_aresta(matriz, vertices, origem, destino):
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)

        return matriz[i][j] == 1

    return False


def vizinhos(matriz, vertices, vertice):
    lista_vizinhos = []

    if vertice not in vertices:
        return lista_vizinhos

    i = vertices.index(vertice)

    for j in range(len(vertices)):
        if matriz[i][j] == 1:
            lista_vizinhos.append(vertices[j])

    return lista_vizinhos


def grau_vertices(matriz, vertices, nao_direcionado=False):
    graus = {}

    for i in range(len(vertices)):
        vertice = vertices[i]

        grau_saida = sum(matriz[i])

        grau_entrada = 0

        for linha in matriz:
            grau_entrada += linha[i]

        if nao_direcionado:
            grau_total = grau_saida + matriz[i][i]
        else:
            grau_total = grau_entrada + grau_saida

        graus[vertice] = {
            "entrada": grau_entrada,
            "saida": grau_saida,
            "total": grau_total
        }

    return graus


def percurso_valido(matriz, vertices, caminho):
    if not caminho:
        return False

    for vertice in caminho:
        if vertice not in vertices:
            return False

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]

        if not existe_aresta(matriz, vertices, origem, destino):
            return False

    return True


def listar_vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        print("Vertice nao encontrado!")
        return

    lista = vizinhos(matriz, vertices, vertice)

    print("Vizinhos de", vertice, ":", lista)


def exibir_grafo(matriz, vertices):
    if not vertices:
        print("Grafo vazio!")
        return

    print("\nMatriz de Adjacencia:")

    largura = max(4, max(len(str(v)) for v in vertices) + 2)

    print(" " * largura, end="")

    for vertice in vertices:
        print(f"{vertice:>{largura}}", end="")

    print()

    for i in range(len(vertices)):
        print(f"{vertices[i]:>{largura}}", end="")

        for j in range(len(vertices)):
            print(f"{matriz[i][j]:>{largura}}", end="")

        print()


def main():
    matriz, vertices = criar_grafo()

    print("===== TIPO DE GRAFO =====")
    print("1 - Direcionado")
    print("2 - Nao direcionado")

    while True:
        tipo = input("Escolha o tipo: ")

        if tipo == "1" or tipo == "2":
            break

        print("Opcao invalida!")

    nao_direcionado = tipo == "2"

    while True:
        print("\n========== MENU GRAFO ==========")
        print("1 - Exibir grafo")
        print("2 - Inserir vertice")
        print("3 - Inserir aresta")
        print("4 - Remover vertice")
        print("5 - Remover aresta")
        print("6 - Listar vizinhos")
        print("7 - Verificar aresta")
        print("8 - Calcular grau dos vertices")
        print("9 - Verificar percurso")
        print("0 - Sair")
        print("================================")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            exibir_grafo(matriz, vertices)

        elif opcao == "2":
            vertice = input("Digite o vertice: ").strip()

            inserir_vertice(matriz, vertices, vertice)

        elif opcao == "3":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()

            inserir_aresta(
                matriz, vertices, origem, destino, nao_direcionado
            )

        elif opcao == "4":
            vertice = input("Vertice para remover: ").strip()

            remover_vertice(matriz, vertices, vertice)

        elif opcao == "5":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()

            remover_aresta(
                matriz, vertices, origem, destino, nao_direcionado
            )

        elif opcao == "6":
            vertice = input("Digite o vertice: ").strip()

            listar_vizinhos(matriz, vertices, vertice)

        elif opcao == "7":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()

            if existe_aresta(matriz, vertices, origem, destino):
                print("A aresta existe!")
            else:
                print("A aresta nao existe!")

        elif opcao == "8":
            graus = grau_vertices(
                matriz, vertices, nao_direcionado
            )

            for vertice in graus:
                print("\nVertice:", vertice)

                if nao_direcionado:
                    print("Grau:", graus[vertice]["total"])
                else:
                    print("Grau de entrada:",
                          graus[vertice]["entrada"])
                    print("Grau de saida:",
                          graus[vertice]["saida"])
                    print("Grau total:",
                          graus[vertice]["total"])

        elif opcao == "9":
            entrada = input(
                "Digite o percurso (ex: A,B,C): "
            )

            caminho = [
                v.strip() for v in entrada.split(",")
            ]

            if percurso_valido(matriz, vertices, caminho):
                print("Percurso valido!")
            else:
                print("Percurso invalido!")

        elif opcao == "0":
            print("Encerrando programa...")
            break

        else:
            print("Opcao invalida!")


if __name__ == "__main__":
    main()