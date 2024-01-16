import os
from fitz import Document, Page, Rect
import fitz
import pandas as pd
from subprocess import run
from time import sleep
from dotenv import load_dotenv
import sys
from a00coordenadas.a00coordenadas import CoordenadasGia
load_dotenv()
sys.path.append('../')
class LeitorDeGia():
    def __init__(self):
        self.sep = '/' if eval(os.getenv('IS_LINUX')) else '\\' # Alterado
        self.base_path = os.path.dirname(os.path.abspath("\a00leitor_dia"))

    def _ininicializador(self, path_dos_arquivos, save):
        self.CoordenadasGia = CoordenadasGia()
        self.CoordenadasGia = self.CoordenadasGia._coordenadas_gia()
        self.campos_documento = {"a00mes_ano_referencia":[], 
                        "a01nome_empresarial" : [],
                        "a02sem_st_no_estado":[],
                        "a03sem_st_com_outros_estado":[],
                        "a04total":[],
                        "a05por_saida_com_debito_imposto":[],
                        "a06nome_arquivo":[]}
        self.path_dos_arquivos = path_dos_arquivos
        self.save = save

    
    def _captura_de_gia(self):
        VISUALIZE = True
        arquivos_pdf = self.path_dos_arquivos
        nome_arquivo = self.path_dos_arquivos.split("\\")[-1]

        lista_arquivos_pdf = [arq for arq in os.listdir(arquivos_pdf) if arq.endswith('.pdf')]
        for arq in lista_arquivos_pdf:
            doc: Document = fitz.open(f"{arquivos_pdf}\\{arq}")
            page: Page = doc[0]
            page.clean_contents()

            for index, ponto in enumerate(self.CoordenadasGia["coord_gia"]):
                rect = Rect(ponto)
                if VISUALIZE:
                    page.draw_rect(rect, width=1.5, color=(0, 0, 1))
                    ponto_capturado = page.get_textbox(rect)
                    if ponto_capturado == "":
                        ponto_capturado = "# #"
                    print(ponto_capturado)
                    if index == 0:
                        self.campos_documento["a00mes_ano_referencia"].append(ponto_capturado)
                    elif index == 1:
                        self.campos_documento["a01nome_empresarial"].append(ponto_capturado)
                    elif index == 2:
                        self.campos_documento["a02sem_st_no_estado"].append(ponto_capturado)
                    elif index == 3:
                        self.campos_documento["a03sem_st_com_outros_estado"].append(ponto_capturado)
                    elif index == 4:
                        self.campos_documento["a04total"].append(ponto_capturado)
                    elif index == 5:
                        self.campos_documento["a05por_saida_com_debito_imposto"].append(ponto_capturado)
                    
            self.campos_documento["a06nome_arquivo"].append(arq)
            print(self.campos_documento)

        df = pd.DataFrame(self.campos_documento)
        print(df)
        df.to_excel(f"{self.save}{self.sep}leitor_de_gia.xlsx", index=False)        

        
    def localizador_de_coordenadas(self, path, descricao):
            
            VISUALIZE = True
            arquivos_pdf = path
            nome_arquivo = path.split("\\")[-1]

            a23_descricao = descricao
            inpu = input

            for arq in os.listdir(arquivos_pdf):
                doc: Document = fitz.open(f"{arquivos_pdf}\\{arq}")
                page: Page = doc[0]
                page.clean_contents()

                if "201111.pdf" in arq:
                    rect = Rect(a23_descricao)
                    if VISUALIZE:
                        page.draw_rect(rect, width=1.5, color=(0, 0, 1))
                        cliente = page.get_textbox(rect)



                        print(type(cliente))
                        print(cliente)
                        output_path = f"b00_localizador_de_coordenadas{0}.pdf"  # Especifique o caminho e nome do arquivo de saída
                        doc.save(output_path)
                        self.abrir_pdf(output_path)
                        break

    def abrir_pdf(self, nome_arquivo):
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

def renomear_arquivos(caminho_pasta):
  """
  Renomeia todos os arquivos em uma pasta.

  Args:
    caminho_pasta: Caminho para a pasta a ser renomeada.
    novo_nome: Novo nome para os arquivos.
  """

  arquivos = os.listdir(caminho_pasta)

  for arquivo in arquivos:
    novo_nome = arquivo.split(" ")
    dia = novo_nome[0]
    ano = novo_nome[1].split(".")[0]
    novo_nome = f"{ano}{dia}"
    novo_caminho = os.path.join(caminho_pasta, f'{novo_nome}.pdf') 
    os.rename(f"{caminho_pasta}\\{arquivo}", novo_caminho)

if __name__ == "__main__":
    app = LeitorDeGia()
    lista = []
    # path = r"_resources_\GIAs"
    path = r"_resources_\GIAs"

    descricao = a23_descricao = (380, 315, 470, 329)
    # renomear_arquivos(path)
    # app.localizador_de_coordenadas(path, descricao)
    app._ininicializador(path, path)
    app._captura_de_gia()