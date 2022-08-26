from bhaskara import bhaskara
from time import sleep
from tabulate import tabulate

a = 0
b = 0
c = 0

def coeficiente():
    calculo = {}
    
    print('Informe os valores da equação, f(x) = ax² + bx + c')
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    print(f'\nEquação: {a}x² + {b}x + {c}')    
    
    calculo = bhaskara(a, b, c)
    
    print(f'Resultado:\nx1 = {calculo["x1"]}\nx2 = {calculo["x2"]}')
    
    sleep(3)
    
def tabela():
    x = 0
    matriz = []
    
    print('Informe os valores da função, f(x) = ax² + bx + c')
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    print(f'\nEquação: {a}*{x}² + {b}*{x} + {c}\n')
    matriz = [["x", f"{a}x² + {b}x + {c}", "f(x)"]]
    
    for i in range(-10, 11):
        fx = a * i**2 + b * i + c
        linha = [i, f"{a}*({i})² + {b}*({i}) + {c}", fx]
        matriz.append(linha)
    
    tabela = tabulate(matriz, headers="firstrow")
    print(tabela)

if __name__ == "__main__":
    opcao = 0
    
    print('Bem vindo ao Função-inator!')
    while True:
        try:
            opcao = int(input('''
(1) Achar coeficientes
(2) Criar tabela
(0) Fechar Programa
> '''))
        except ValueError:
            print('Opção Inválida')
        else:
            match opcao:
                case 1:
                    coeficiente()
                case 2:
                    tabela()
                case 0:
                    break
                case _:
                    print('Opção Inválida')