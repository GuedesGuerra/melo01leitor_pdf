import PySimpleGUI as sg
from a00main import LeitorDeGia

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
            aLeitorDeGia = LeitorDeGia()
            aLeitorDeGia._ininicializador(path, save)
            aLeitorDeGia._captura_de_gia()
            break

    window.close()

open_folder()
