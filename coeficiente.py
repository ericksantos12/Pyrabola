from bhaskara import bhaskara
from time import sleep

def coeficiente(a, b, c):
    calculo = {}
    
    print(f'\nEquação: {a}x² + {b}x + {c}')    
    
    calculo = bhaskara(a, b, c)
    
    print(f'Resultado:\nx1 = {calculo["x1"]}\nx2 = {calculo["x2"]}')
    
    sleep(3)