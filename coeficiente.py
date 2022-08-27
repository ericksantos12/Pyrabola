from bhaskara import bhaskara
from time import sleep

def coeficiente(a, b, c):
    """Imprime na tela as raizes de uma equação de 2º grau

    Args:
        a (integer): Primeiro coeficiente da equação
        b (integer): Segundo coeficiente da equação
        c (integer): Terceiro coeficiente da equação
    """
    
    calculo = {}
    
    print(f'\nEquação: {a}x² + {b}x + {c}')    
    
    calculo = bhaskara(a, b, c)
    
    print(f'Resultado:\nx1 = {calculo["x1"]}\nx2 = {calculo["x2"]}')
    
    sleep(3)