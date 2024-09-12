import numpy as np


tamanho_matriz = 6
valor_minimo = 0
valor_maximo = 1


def criar_e_salvar_matriz():
    global tamanho_matriz, valor_minimo, valor_maximo

    matriz = np.random.randint(
        valor_minimo, valor_maximo + 1, (tamanho_matriz, tamanho_matriz)
    )

    np.savetxt("matriz.txt", matriz, fmt="%d", delimiter=" ")
    print(
        f"Matriz {tamanho_matriz}x{tamanho_matriz} criada e salva no arquivo 'matriz.txt':\n"
    )
    print(matriz)


def ler_matriz():
    try:
        matriz = np.loadtxt("matriz.txt", dtype=int)
        print("\nMatriz carregada do arquivo:\n", matriz)
        return matriz
    except FileNotFoundError:
        print("Erro: O arquivo 'matriz.txt' não foi encontrado.")
        return None


def detectar_padrao(matrix, patterns):
    encontrados = []

    for pattern in patterns:
        padrao_encontrado = False
        padrao_posicoes = []
        soma_total = 0

        for i in range(matrix.shape[0] - pattern.shape[0] + 1):
            for j in range(matrix.shape[1] - pattern.shape[1] + 1):
                sub_matrix = matrix[i : i + pattern.shape[0], j : j + pattern.shape[1]]
                if np.array_equal(sub_matrix, pattern):
                    padrao_encontrado = True
                    padrao_posicoes.append((i, j))
                    soma_total += np.sum(sub_matrix)

        encontrados.append((pattern, padrao_encontrado, padrao_posicoes, soma_total))

    for idx, (pattern, encontrado, posicoes, soma) in enumerate(encontrados):
        padrao_nome = chr(65 + idx)  # A, B, C, ...
        if encontrado:
            print(f"\nPadrão '{padrao_nome}' encontrado nas posições: {posicoes}")
            print(f"Soma dos valores encontrados: {soma}")
            mostrar_padroes(matrix, pattern, posicoes)
        else:
            print(f"\nNenhum padrão '{padrao_nome}' encontrado.")


def mostrar_padroes(matrix, pattern, posicoes):
    visual_matrix = matrix.astype(str)
    for pos in posicoes:
        i, j = pos
        for pi in range(pattern.shape[0]):
            for pj in range(pattern.shape[1]):
                if pattern[pi, pj] == 1:
                    visual_matrix[i + pi, j + pj] = "*"

    print("\nMatriz com padrões destacados:")
    for linha in visual_matrix:
        print(" ".join(linha))


def main():
    global tamanho_matriz, valor_minimo, valor_maximo

    while True:
        print("\nEscolha uma opção:")
        print("1. Criar e salvar uma nova matriz")
        print("2. Carregar matriz do arquivo e mostrar")
        print("3. Detectar padrões 'Y'")
        print("4. Detectar padrões 'T_Normal'")
        print("5. Detectar padrões 'T_Invertido'")
        print("6. Detectar padrões 'T_Normal com T_Invertido'")
        print("7. Detectar todos os padrões")
        print("8. Configurar intervalo de valores para a matriz")
        print("9. Configurar dimensão da matriz")
        print("10. Sair")

        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            criar_e_salvar_matriz()
        elif escolha == "2":
            matriz = ler_matriz()
        elif escolha == "3":
            matriz = ler_matriz()
            if matriz is not None:
                detectar_padrao(matriz, [np.array([[0, 1], [1, 1]])])
        elif escolha == "4":
            matriz = ler_matriz()
            if matriz is not None:
                detectar_padrao(matriz, [np.array([[0, 1, 0], [1, 1, 1], [0, 0, 0]])])
        elif escolha == "5":
            matriz = ler_matriz()
            if matriz is not None:
                detectar_padrao(matriz, [np.array([[0, 0, 0], [1, 1, 1], [0, 1, 0]])])
        elif escolha == "6":
            matriz = ler_matriz()
            if matriz is not None:
                detectar_padrao(
                    matriz,
                    [
                        np.array([[0, 1, 0], [1, 1, 1], [0, 0, 0]]),
                        np.array([[0, 0, 0], [1, 1, 1], [0, 1, 0]]),
                    ],
                )
        elif escolha == "7":
            matriz = ler_matriz()
            if matriz is not None:
                detectar_padrao(
                    matriz,
                    [
                        np.array([[0, 1], [1, 1]]),
                        np.array([[0, 1, 0], [1, 1, 1], [0, 0, 0]]),
                        np.array([[0, 0, 0], [1, 1, 1], [0, 1, 0]]),
                    ],
                )
        elif escolha == "8":
            valor_minimo = int(input("Digite o valor mínimo para a matriz: "))
            valor_maximo = int(input("Digite o valor máximo para a matriz: "))
            print(
                f"Intervalo de valores ajustado para {valor_minimo} a {valor_maximo}."
            )
        elif escolha == "9":
            tamanho_matriz = int(
                input("Digite o tamanho da matriz (por exemplo, 6 para 6x6): ")
            )
            print(f"Tamanho da matriz ajustado para {tamanho_matriz}x{tamanho_matriz}.")
        elif escolha == "10":
            print("Saindo...")
            break
        else:
            print("Escolha inválida, tente novamente.")


if __name__ == "__main__":
    main()
