import PySimpleGUI as sg
from main import localizador_de_coordenadas

def open_folder():
    layout = [
        [sg.Text("Selecione uma pasta:")],
        [sg.InputText(key="-FOLDER-"), sg.FolderBrowse()],
        [sg.Button("OK"), sg.Button("Cancelar")]
    ]

    window = sg.Window("Selecione uma pasta", layout)

    while True:
        event, values = window.read()
        values = [valor for valor in values.values()]
        print(values)
        if event in (sg.WIN_CLOSED, "Cancelar"):
            break
        elif event == "OK":
            lista=[]
            path = values[0]
            save = values[0]
            descricao = a23_descricao = (30, 420, 350, 480)

            localizador_de_coordenadas(path, descricao, lista, 3, save)
            # sg.popup;(f"Pasta selecionada: {folder_selected}")
            break

    window.close()

open_folder()
