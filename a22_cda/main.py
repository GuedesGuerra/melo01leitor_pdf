import os
from fitz import Document, Page, Rect
import fitz
import pandas as pd
from subprocess import run
from time import sleep
def localizador_de_coordenadas(path, descricao, lista, input, save):
        dicionario = {"Principal":[], 
                      "Multa" : [],
                      "Juros de mora":[],
                      "Encargo Legal":[],
                      "Valor Total":[],
                      "nome_arquivo":[]}
        VISUALIZE = True
        arquivos_pdf = path
        nome_arquivo = path.split("\\")[-1]

        a23_descricao = descricao
        inpu = input

        for arq in os.listdir(arquivos_pdf):
            doc: Document = fitz.open(f"{nome_arquivo}\\{arq}")
            page: Page = doc[0]
            page.clean_contents()

            rect = Rect(a23_descricao)
            if VISUALIZE:
                page.draw_rect(rect, width=1.5, color=(0, 0, 1))
                cliente = page.get_textbox(rect)
                cliente = cliente.split("\n")

                for i in cliente:
                    if "Principal" in i:
                        principal = i.split("R$ ")[-1]
                        dicionario["Principal"].append(principal)
                    elif "Multa" in i:
                        multa = i.split("R$ ")[-1]
                        dicionario["Multa"].append(multa)
                    elif "Juros de Mora" in i:
                        juros_de_mora = i.split("R$ ")[-1]
                        dicionario['Juros de mora'].append(juros_de_mora)
                    elif "Encargo Legal" in i:
                        encargo_legal = i.split("R$ ")[-1]
                        dicionario["Encargo Legal"].append(encargo_legal)
                    elif "Valor Total" in i:
                        valor_total = i.split("R$ ")[-1]
                        dicionario["Valor Total"].append(valor_total)
                        dicionario["nome_arquivo"].append(arq)
        
        df = pd.DataFrame(dicionario)
        df.to_excel(f"{save}\\a00_consulta_cda.xlsx", index=False)


        #     print(type(cliente))
        #     print(cliente)
        # output_path = f"b00_localizador_de_coordenadas{0}.pdf"  # Especifique o caminho e nome do arquivo de saída
        # doc.save(output_path)
        # abrir_pdf(output_path)

def abrir_pdf(nome_arquivo):
    try:
        run(['xdg-open', nome_arquivo])  # Linux
        
    except FileNotFoundError:
        try:
            run(['open', nome_arquivo])  # macOS
        except FileNotFoundError:
            run(['start', '', nome_arquivo], shell=True)  # Windows
            sleep(1)

def planilhar_files(path, name):
    dtype = {"a02_numero_cod_barra": str}
    df = pd.read_json(path, dtype=dtype)
    df = pd.DataFrame(df)
    df.to_excel(f'{name}.xlsx', index=False)

if __name__ == "__main__":
    ...
    # lista = []
    # path = r"modelo_cda\a00.pdf"

    # descricao = a23_descricao = (30, 420, 350, 480)

    # localizador_de_coordenadas(path, descricao, lista, 3)