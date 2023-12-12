import PySimpleGUI as sg
from main import localizador_de_coordenadas
from a00textos_para_pdf import txt_to_pdf

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

def open_txt():
    layout = [
        [sg.Text("Selecione a pasta que contém os arquivos .txt:")],
        [sg.InputText(key="-TXT-"), sg.FolderBrowse()],
        [sg.Text("Selecione a pasta para salvar os arquivos .txt:")],
        [sg.InputText(key="-TXT-"), sg.FolderBrowse()],
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

            path = values[0]
            save = values[2]
            txt_to_pdf(path, save)
            # sg.popup;(f"Pasta selecionada: {folder_selected}")
            break

    window.close()

sg.theme("LightGrey1")

layout = [
    [sg.Button("Selecionar Pasta", key="-FOLDER-"), sg.Button("Selecionar Arquivo de Texto", key="-TXT-")]
]

window = sg.Window("Minha Interface", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-FOLDER-":
        open_folder()  # Chama a função open_folder quando o botão "Selecionar Pasta" é pressionado
    elif event == "-TXT-":
        open_txt()  # Chama a função open_txt quando o botão "Selecionar Arquivo de Texto" é pressionado

window.close()
