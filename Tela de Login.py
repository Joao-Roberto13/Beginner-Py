from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]

#Windows
janela = sg.Window('Tela de Login', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'João Roberto' and valores['senha'] == '123456':
            print('Bem vindo ao Jogo de Advinha!')
            K = input("Press Enter")
