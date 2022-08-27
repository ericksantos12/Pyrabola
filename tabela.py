from tabulate import tabulate
from time import sleep

def tabela(a, b, c):
    """Método para imprimir a tabela de criação de gráfico de uma função quadrática

    Args:
        a (integer): Primeiro coeficiente da função
        b (integer): Segundo coeficiente da função
        c (integer): Terceiro coeficiente da função
    """
    
    x = 0
    matriz = []
    
    print('Informe os valores da função, f(x) = ax² + bx + c')
    
    print(f'\nEquação: {a}*{x}² + {b}*{x} + {c}\n')
    matriz = [["x", f"{a}x² + {b}x + {c}", "f(x)"]]
    
    for i in range(-10, 11):
        fx = a * i**2 + b * i + c
        linha = [i, f"{a}*({i})² + {b}*({i}) + {c}", fx]
        matriz.append(linha)
    
    tabela = tabulate(matriz, headers="firstrow")
    print(tabela)
    
    sleep(3)