from coeficiente import coeficiente
from tabela import tabela

def menu():
    return int(input('''
(1) Alterar valores
(2) Achar coeficientes
(3) Criar tabela
(0) Fechar Programa
> '''))

def pedirValores():
    global _a
    global _b
    global _c
    print('Informe os valores da função, f(x) = ax² + bx + c')
    _a = int(input('a = '))
    _b = int(input('b = '))
    _c = int(input('c = '))
    

if __name__ == "__main__":
    opcao = 0
    
    print('Bem vindo ao Função-inator!')
    while True:
        try:
            opcao = menu()
        except ValueError:
            print('Opção Inválida')
        else:
            match opcao:
                case 1:
                    pedirValores()
                case 2:
                    coeficiente(_a, _b, _c)
                case 3:
                    tabela(_a, _b, _c)
                case 0:
                    print('PROGRAMA ENCERRADO')
                    break
                case _:
                    print('Opção Inválida')