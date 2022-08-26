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
                print('opcao 1')
            case 2:
                print('opcao 2')
            case 0:
                break
            case _:
                print('Opção invalida')