from bhaskara import bhaskara
from time import sleep

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
    
    calculo = bhaskara(a, b, c)
    
    print(f'Resultado:\nx1 = {calculo["x1"]}\nx2 = {calculo["x2"]}')
    
    sleep(3)
    

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
                    print('opcao 2')
                case 0:
                    break
                case _:
                    print('Opção Inválida')