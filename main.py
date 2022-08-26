from math import sqrt
from time import sleep

def bhaskara(a, b, c):
    x1 = 0
    x2 = 0
    delta = pow(b, 2) - 4 * a * c
    
    try:
        x1 = (-b + sqrt(delta)) / 2*a
        x2 = (-b - sqrt(delta)) / 2*a
    except ValueError:
        return {
            "x1": 'Indefinido',
            "x2": 'Indefinido'
        }
    else:
        return {
            "x1": x1,
            "x2": x2
        }

def coeficiente():
    a = 0
    b = 0
    c = 0
    calculo = {}
    
    print('Informe os valores da equação, f(x) = ax² + bx + c')
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    print(f'\nEquação: {a}x² + {b}x + {c}')
    sleep(1)
    
    calculo = bhaskara(a, b, c)
    print(f'Resultado:\nx1 = {calculo["x1"]}\nx2 = {calculo["x2"]}')
    

if __name__ == "__main__":
    opcao = 0
    
    print('Bem vindo ao Função-inator!')
    while True:
        opcao = int(input('''
(1) Achar coeficientes
(2) Criar tabela
(0) Fechar Programa
> '''))
        match opcao:
            case 1:
                coeficiente()
            case 2:
                print('opcao 2')
            case 0:
                break
            case _:
                print('Opção invalida')