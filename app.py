from bhaskara import bhaskara
import PySimpleGUI as sg

def main():
    #Layout

    coluna1 = [
        [sg.Text('Insira os coeficientes:')],
        [sg.Text('A'), sg.Input(key='-inputA-', size=7), sg.Button('Raizes')],
        [sg.Text('B'), sg.Input(key='-inputB-', size=7), sg.Button('Grafico')],
        [sg.Text('C'), sg.Input(key='-inputC-', size=7)],
        [sg.Text('Resultado:')],
        [sg.Text('X1: '), sg.Text(key='-outputA-')],
        [sg.Text('X2: '), sg.Text(key='-outputB-')]
    ]
    coluna2 = [
        [sg.Text('Gráfico da Função:')],
        [sg.Multiline(size=(20,10))]
    ]
    
    layout = [
        [sg.Column(coluna1), sg.VerticalSeparator(), sg.Column(coluna2)],
        [sg.Push(), sg.Text(key='-debug-'), sg.Push()]
    ]
    
    #Criação da janela
    window = sg.Window('Pyrabola', layout)
    
    #Loop de eventos
    while True:
        event, values = window.read()
        a = 0
        b = 0
        c = 0
        raizes = {}
        
        if event == sg.WIN_CLOSED:
            break
        if event == 'Raizes':
            window['-debug-'].update('')
            try:
                a = int(values['-inputA-'])
                b = int(values['-inputB-'])
                c = int(values['-inputC-'])
            
                raizes = bhaskara(a, b, c)
                
                window['-outputA-'].update(raizes['x1'])
                window['-outputB-'].update(raizes['x2'])
            except ValueError:
                window['-debug-'].update('Insira os valores (╥︣﹏᷅╥)')
            
            
    
    window.close()

if __name__ == "__main__":
    main()