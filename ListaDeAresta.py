def criar_grafo():
    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        print("Vertice inserido com sucesso!")
    else:
        print("Vertice ja existe!")


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(vertices, origem)

    if destino not in vertices:
        inserir_vertice(vertices, destino)

    if existe_aresta(arestas, origem, destino, nao_direcionado):
        print("Aresta ja existe!")
        return

    arestas.append((origem, destino))
    print("Aresta inserida com sucesso!")


def remover_vertice(vertices, arestas, vertice):
    if vertice not in vertices:
        print("Vertice nao encontrado!")
        return

    vertices.remove(vertice)

    for aresta in arestas[:]:
        if vertice in aresta:
            arestas.remove(aresta)

    print("Vertice removido com sucesso!")


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if (origem, destino) in arestas:
        arestas.remove((origem, destino))

    elif nao_direcionado and (destino, origem) in arestas:
        arestas.remove((destino, origem))

    else:
        print("Aresta nao encontrada!")
        return

    print("Aresta removida com sucesso!")


def existe_aresta(arestas, origem, destino, nao_direcionado=False):
    if (origem, destino) in arestas:
        return True

    if nao_direcionado and (destino, origem) in arestas:
        return True

    return False


def vizinhos(arestas, vertice, nao_direcionado=False):
    lista_vizinhos = []

    for origem, destino in arestas:
        if origem == vertice:
            lista_vizinhos.append(destino)

        if nao_direcionado and destino == vertice and origem != destino:
            lista_vizinhos.append(origem)

    return lista_vizinhos


def listar_vizinhos(vertices, arestas, vertice, nao_direcionado=False):
    if vertice not in vertices:
        print("Vertice nao encontrado!")
        return

    lista = vizinhos(arestas, vertice, nao_direcionado)
    print("Vizinhos de", vertice, ":", lista)


def exibir_grafo(vertices, arestas):
    if not vertices:
        print("Grafo vazio!")
        return

    print("\nLista de Arestas:")

    for origem, destino in arestas:
        print(origem, "->", destino)

    if not arestas:
        print("Nenhuma aresta cadastrada!")

    print("\nVertices:", vertices)


def grau_vertices(vertices, arestas, nao_direcionado=False):
    graus = {}

    for vertice in vertices:
        grau_entrada = 0
        grau_saida = 0

        for origem, destino in arestas:
            if origem == vertice:
                grau_saida += 1

            if destino == vertice:
                grau_entrada += 1

        if nao_direcionado:
            grau_total = grau_entrada + grau_saida
        else:
            grau_total = grau_entrada + grau_saida

        graus[vertice] = {
            "entrada": grau_entrada,
            "saida": grau_saida,
            "total": grau_total
        }

    return graus


def percurso_valido(vertices, arestas, caminho, nao_direcionado=False):
    if not caminho:
        return False

    for vertice in caminho:
        if vertice not in vertices:
            return False

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]

        if not existe_aresta(arestas, origem, destino, nao_direcionado):
            return False

    return True


def main():
    vertices, arestas = criar_grafo()

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
            exibir_grafo(vertices, arestas)

        elif opcao == "2":
            vertice = input("Digite o vertice: ").strip()
            inserir_vertice(vertices, vertice)

        elif opcao == "3":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()

            inserir_aresta(
                vertices, arestas, origem, destino, nao_direcionado
            )

        elif opcao == "4":
            vertice = input("Vertice para remover: ").strip()
            remover_vertice(vertices, arestas, vertice)

        elif opcao == "5":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()

            remover_aresta(
                arestas, origem, destino, nao_direcionado
            )

        elif opcao == "6":
            vertice = input("Digite o vertice: ").strip()

            listar_vizinhos(
                vertices, arestas, vertice, nao_direcionado
            )

        elif opcao == "7":
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()

            if existe_aresta(arestas, origem, destino, nao_direcionado):
                print("A aresta existe!")
            else:
                print("A aresta nao existe!")

        elif opcao == "8":
            graus = grau_vertices(
                vertices, arestas, nao_direcionado
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

            if percurso_valido(
                vertices, arestas, caminho, nao_direcionado
            ):
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