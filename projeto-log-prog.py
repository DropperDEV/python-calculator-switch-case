
def soma():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    r = n1 + n2
    print(r)


def sub():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    r = n1 - n2
    print(r)


def mult():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    r = n1 * n2
    print(r)


def div():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    r = n1 / n2
    print(r)


def expo():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    r = n1 ** n2
    print(r)


while True:
    print()
    print('Calculadora-Multi-Funções\n')
    print()
    print('Soma - ( 1 ) \n')
    print('Subtração - ( 2 )\n')
    print('Multiplicação - ( 3 )\n')
    print('Divisão - ( 4 )\n')
    print('Exponenciação - ( 5 )\n')

    escolha = int(input(''))
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
        case _:
            print('Número inválido\n')
