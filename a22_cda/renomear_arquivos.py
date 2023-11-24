import os
from fitz import Document, Page, Rect
import fitz
# from a01coordenadas.a00coordenadas import coordenadas_comprovante3e
import pandas as pd
from subprocess import run
# from a01coordenadas.a00coordenadas import CoordenadasComprovanteModelo2
# from a01coordenadas.a00coordenadas import CoordenadasComprovanteModelo1
from time import sleep
def renomear_arquivos_em_pasta(pasta):

        # Itera sobre todos os arquivos na pasta
        for nome_arquivo in os.listdir(pasta):
            if "GUIA" in nome_arquivo or "guia" in nome_arquivo:
                caminho_atual = os.path.join(pasta, nome_arquivo)

                # Verifica se o item é um arquivo (não um diretório)
                if os.path.isfile(caminho_atual):
                    # Extrai a extensão do arquivo original
                    _, extensao = os.path.splitext(nome_arquivo)
                    novo_nome = f"boleto_banco_caixa_modelo_2_{_}"
                    # Cria o novo nome do arquivo com a extensão original
                    novo_nome_arquivo = f"{novo_nome}{extensao}"

                    # Cria o novo caminho com o novo nome no mesmo diretório
                    novo_caminho = os.path.join(pasta, novo_nome_arquivo)

                    # Renomeia o arquivo
                    os.rename(caminho_atual, novo_caminho)
                    print(f"Arquivo renomeado para {novo_nome_arquivo}")

            if "COMP" in nome_arquivo or "comp" in nome_arquivo:
                caminho_atual = os.path.join(pasta, nome_arquivo)

                # Verifica se o item é um arquivo (não um diretório)
                if os.path.isfile(caminho_atual):
                    # Extrai a extensão do arquivo original
                    _, extensao = os.path.splitext(nome_arquivo)
                    novo_nome = f"comprovante_{_}"
                    # Cria o novo nome do arquivo com a extensão original
                    novo_nome_arquivo = f"{novo_nome}{extensao}"

                    # Cria o novo caminho com o novo nome no mesmo diretório
                    novo_caminho = os.path.join(pasta, novo_nome_arquivo) # pdfs_de_teste é pasta que sera salvo

                    # Renomeia o arquivo
                    os.rename(caminho_atual, novo_caminho)
                    print(f"Arquivo renomeado para {novo_nome_arquivo}")

def localizador_de_coordenadas(path, descricao, lista, input):
        # aCoordenadasComprovanteModelo1 = CoordenadasComprovanteModelo1()
        # bCoordenadasComprovanteModelo2 = CoordenadasComprovanteModelo2()
        # aCoordenadasComprovanteModelo1 = aCoordenadasComprovanteModelo1._comprovante_modelo1()
        # bCoordenadasComprovanteModelo2 = bCoordenadasComprovanteModelo2._comprovante_modelo2()
        dicionario = {"path":[], "texto" : []}
        VISUALIZE = True
        arquivos_pdf = path
        # arquivos_pdf = r"modelos_arquivos_pdfs\a00_teste\comprovante_D ANTERO - COMP.PDF"
        a23_descricao = descricao
        inpu = input

        doc: Document = fitz.open(arquivos_pdf)
        page: Page = doc[0]
        page.clean_contents()
        if inpu < 2:
            for i in aCoordenadasComprovanteModelo1["coord_comprovante"]:
                rect = Rect(i)
                if VISUALIZE:
                    page.draw_rect(rect, width=1.5, color=(0, 0, 1))
                    cliente = page.get_textbox(rect)
                    print(cliente)
        elif inpu == 5:
            a = 0
            for i in lista:
                doc: Document = fitz.open(i)
                page: Page = doc[0]
                page.clean_contents()
                rect = Rect(a23_descricao)
                if VISUALIZE:
                    page.draw_rect(rect, width=1.5, color=(0, 0, 1))
                    cliente = page.get_textbox(rect)
                    print(cliente)
                    dicionario["path"].append(i)
                    dicionario["texto"].append(cliente)
                    i = i.split("\\")[-1]
                    output_path = f"b00{i}"  # Especifique o caminho e nome do arquivo de saída
                    a = a + 1
                    doc.save(output_path)
                    abrir_pdf(output_path)
            df = pd.DataFrame(dicionario)
            df.to_excel("dicionario.xlsx", index=False)
        else:

            rect = Rect(a23_descricao)
            if VISUALIZE:
                page.draw_rect(rect, width=1.5, color=(0, 0, 1))
                cliente = page.get_textbox(rect)
                print(cliente)
        output_path = f"b00_localizador_de_coordenadas{0}.pdf"  # Especifique o caminho e nome do arquivo de saída
        doc.save(output_path)
        abrir_pdf(output_path)
        # cliente = page.get_textbox(rect)
        print()

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

lista = [
        "teste_de_execucao\\comprovante_Admilson Dias - COMP.pdf",
        "teste_de_execucao\\comprovante_Adriano Tavares - COMP.pdf",
        "teste_de_execucao\\comprovante_Amado & Ribas - COMP.pdf",
        "teste_de_execucao\\comprovante_Antonio Alves - COMP.pdf",
        "teste_de_execucao\\comprovante_Antonio Luis - COMP.pdf",
        "teste_de_execucao\\comprovante_Evandro Marques - COMP.pdf",
        "teste_de_execucao\\comprovante_Ewerton Fabiano - COMP.pdf",
        "teste_de_execucao\\comprovante_J. Magalhaes - COMP.pdf",
        "teste_de_execucao\\comprovante_Jociane Aparecida - COMP.pdf",
        "teste_de_execucao\\comprovante_Luciano Rodrigues - COMP.pdf",
        "teste_de_execucao\\comprovante_Snt Com\u00e9rcio Logistica - COMP.pdf",
        "teste_de_execucao\\comprovante_Sollucions Business - COMP.pdf",
        "teste_de_execucao\\comprovante_Supermercado Pre\u00e7o - COMP.pdf",
        "teste_de_execucao\\comprovante_Valdemir Prachedes - COMP.pdf"
    ]
# Exemplo de uso:
pasta = r"teste_de_execucao"
novo_nome = "novo_nome"
# renomear_arquivos_em_pasta(pasta)
path = r"modelo_cda\a00.pdf"
#boleto_banco_caixa_modelo_3_Baselog Operador Logístico - GUIA.pdf
descricao = a23_descricao = (30, 420, 350, 480)
# (139, 270, 550, 290)
localizador_de_coordenadas(path, descricao, lista, 3)
# path = r"bd01_banco_dados\a00banco_dados_de_boletos.json"
path = r"bd01_banco_dados\a00banco_dados_de_comprovantes.json"
name = "comprovante"
# planilhar_files(path, name)
