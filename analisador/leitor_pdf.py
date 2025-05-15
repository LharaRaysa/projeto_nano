import os
import fitz

class PDFLoader:
    def __init__(self, pasta):
        self.pasta = pasta

    def carregar_textos(self):
        textos = {}
        for arquivo in os.listdir(self.pasta):
            if arquivo.endswith(".pdf"):
                caminho = os.path.join(self.pasta, arquivo)
                textos[arquivo] = self.extrair_texto(caminho)
        return textos

    def extrair_texto(self, caminho_pdf):
        texto = ""
        with fitz.open(caminho_pdf) as doc:
            for pagina in doc:
                texto += pagina.get_text()
        return texto
