
# CALCULADORA
def calc():
    def soma():
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
        print(n1 + n2)

    def sub():
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
        print(n1 - n2)

    def mult():
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
        print(n1 * n2)

    def div():
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
        print(n1 / n2)

    def expo():
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
        print(n1 ** n2)

    def rad():
        n1 = int(input('Digite um número: '))
        print(n1**(1/2))
    while True:
        print()
        print('Calculadora-Multi-Funções\n')
        print()
        print('Soma - ( 1 )')
        print('Subtração - ( 2 )')
        print('Multiplicação - ( 3 )')
        print('Divisão - ( 4 )')
        print('Exponenciação - ( 5 )')
        print('Radiciação !Quad! - ( 6 )')

        escolha = int(input(': '))
        match escolha:
            case 1:
                soma()
                break
            case 2:
                sub()
                break
            case 3:
                mult()
                break
            case 4:
                div()
                break
            case 5:
                expo()
                break
            case 6:
                rad()
                break
            case _:
                print('Número inválido\n')


# TABUADA
def table():
    print('*'*30)
    print('TABUADA MULTIPLICAÇÃO')
    print('*'*30)
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = int(input("Digite o número:"))
    for item in n:
        print(f'{item}x{m} = {item*m}')


# MAIOR NÚMERO q-7
def mnumero():
    lista = []

    qtn = int(input('informe a quantidade de numeros: '))

    for i in range(0, qtn):
        lista.append(int(input('Digite o número: ')))

    print(f'Maior número da lista: {max(lista)}')


# FATORIAL 1 A 16 q-20
def fatorial():
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Voce quer a fatorial de quantos numeros: '))
        if quantidade <= 0:
            print('Quantidade deve ser positiva!')

    for i in range(0, quantidade):
        termo = 0
        while (termo <= 0) or (termo > 16):
            termo = int(input('Voce quer o fatorial de qual termo: '))
            if termo <= 0:
                print('O termo deve ser positivo!')
            if termo > 16:
                print('O termo deve ser menor que 16')

        fatorial = 1
        for i in range(1, termo + 1):
            fatorial *= i

        print(fatorial)


# PANIFICADORA-30
def panific():
    print('=' * 16)
    print("Panificadora Pão de Ontem - Tabela de preços")
    print('=' * 16)

    p = float(input("Adicione o preço do pão:\n"))

    print(f"preço do pão: {p} reais")

    for q in range(1, 51):
        print(f'{q} -{p * q:.2f}')

# INFO ALUNOS ACADEMIA-37
def academia():
    cod_clientes = []
    altura_clientes = []
    peso_clientes = []
    n_cliente = 1
    codigo = True

    while codigo != 0:
        print("\nCliente n° ", n_cliente)
        codigo = int(input("Digite o código: "))
        if codigo == 0:
            break
        else:
            altura = float(input("Digite a altura: "))
            peso = float(input("Digite o peso: "))
            cod_clientes.append(codigo)
            altura_clientes.append(altura)
            peso_clientes.append(peso)
            n_cliente += 1

    cod_magro = peso_clientes.index(min(peso_clientes))
    cod_gordo = peso_clientes.index(max(peso_clientes))
    cod_alto = altura_clientes.index(max(altura_clientes))
    cod_baixo = altura_clientes.index(min(altura_clientes))

    print("\n" * 5)
    print(f"Código do mais magro:{cod_clientes[cod_magro]}")
    print(f"Código do mais gordo:{cod_clientes[cod_gordo]}")
    print(f"Código do mais alto:{cod_clientes[cod_alto]}")
    print(f"Código do mais baixo:{cod_clientes[cod_baixo]}")
    print(f"Média de altura:{sum(altura_clientes) / len(altura_clientes)}")
    print(f"Média de peso:{sum(peso_clientes) / len(peso_clientes)}")


# INFO CARROS-40
def carros():
    cod_cidades = []
    n_veiculos = []
    n_acidentes = []
    acidentes_1999 = []

    for i in range(2):
        print("\nCidade número ", i + 1)
        codigo_cidade = int(input("Digite o código da cidade: "))
        while codigo_cidade in cod_cidades:
            print("[Código já digitado]")
            codigo_cidade = int(input("Digite outro código: "))

        numero_acidentes = int(input("Digite o número de acidentes: "))
        numero_veiculos = int(input("Digite o número de veiculos: "))

        if numero_veiculos > 2000:
            acidentes_1999.append(numero_acidentes)
            n_acidentes.append(numero_acidentes)
        else:
            n_acidentes.append(numero_acidentes)

        n_veiculos.append(numero_veiculos)
        cod_cidades.append(codigo_cidade)

    ind_acide_menor = n_acidentes.index(min(n_acidentes))
    ind_acide_maior = n_acidentes.index(max(n_acidentes))

    print(f"\nMenos acidentes\nQuantidade de acidentes:{min(n_acidentes)}\nCódigo da cidade:{cod_cidades[ind_acide_menor]}")
    print(f"\nMais acidentes\nQuantidade de acidentes:{max(n_acidentes)}\nCódigo da cidade:{cod_cidades[ind_acide_maior]}")

    media_veiculos = sum(n_veiculos) / len(n_veiculos)
    print(f"\nMédia de veiculos nas 5 cidades:{media_veiculos}")

    media_acidentes_2000 = sum(acidentes_1999) / len(acidentes_1999)
    print(f"\nMédia de acidentes nas cidades com menos de 2000 veículos:{media_acidentes_2000}")


while True:
    print()
    print('Coletânea de Programas\n')
    print()
    print('Calculadora - ( 1 )')
    print('Tabuada - ( 2 )')
    print('Leitor de Número Maior - ( 3 )')
    print('Fatorial até 16 - ( 4 )')
    print('Tabela de preço pão - ( 5 )')
    print('Dados Alunos - ( 6 )')
    print('Dados veiculares - ( 7 )\n')

    escolha = int(input("Escolha um número: \n"))
    match escolha:
        case 1:
            calc()
            print()
        case 2:
            table()
            print()
        case 3:
            mnumero()
            print()
        case 4:
            fatorial()
            print()
        case 5:
            panific()
            print()
        case 6:
            academia()
            print()
        case 7:
            carros()
            print()
        case _:
            print("Número inválido!")
