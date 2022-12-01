
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
