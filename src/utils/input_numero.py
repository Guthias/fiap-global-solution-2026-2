def apagar_linhas(n):
    for _ in range(n):
        print("\033[F\033[K", end="")

def input_numero(texto):
    while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print("Valor invalido. Por favor, digite um número inteiro.\n")
            input("Pressione Enter para continuar...")
            apagar_linhas(4)