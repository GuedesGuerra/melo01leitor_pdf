from fpdf import FPDF

def fix_text(text):
    # Aqui você pode implementar sua lógica para substituir ou remover caracteres problemáticos
    # Exemplo: substituir o caractere '\ufffd' por um espaço em branco
    return text.replace('\ufffd', ' ')

def txt_to_pdf(txt_file, save):
    from glob import glob
    for i in glob(f"{txt_file}\\*.txt"):
        pdf = FPDF()
        pdf.add_page(orientation='L')
        pdf.set_font("Arial", size=8)
        nome_txt = i.split("\\")[-1]
        nome_txt = nome_txt.split(".")[0]
        with open(i, "r", encoding="ISO-8859-1") as file:
            for line in file:
                if line.startswith("|"):
                # Corrigir o texto da linha, se necessário
                    corrected_line = fix_text(line)
                    pdf.cell(280, 7, txt=corrected_line, ln=True)

        pdf.output(f"{save}\\{nome_txt}.pdf")


if __name__ == "__main__":
    ...
    txt_file = "SPED FISCAL"
    pdf_file = "_save"

    txt_to_pdf(txt_file, pdf_file)

