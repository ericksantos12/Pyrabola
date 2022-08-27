from coeficiente import coeficiente
from tabela import tabela
import PySimpleGUI as sg

def main():
    #Layout

    coluna1 = [
        [sg.Text('Insira os coeficientes:')],
        [sg.Text('A'), sg.Input(key='-inputA-', size=7), sg.Button('Raizes')],
        [sg.Text('B'), sg.Input(key='-inputB-', size=7), sg.Button('Grafico')],
        [sg.Text('C'), sg.Input(key='-inputC-', size=7)],
        [sg.Text('Resultado:'), sg.Text('')]
    ]
    coluna2 = [
        [sg.Text('Gráfico da Função:')],
        [sg.Multiline(size=(20,10))]
    ]
    
    layout = [
        [sg.Column(coluna1), sg.VerticalSeparator(), sg.Column(coluna2)]
    ]
    
    #Criação da janela
    window = sg.Window('Pyrabola', layout)
    
    #Loop de eventos
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
    
    window.close()

if __name__ == "__main__":
    main()