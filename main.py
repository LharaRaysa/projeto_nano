from analisador.leitor_pdf import PDFLoader
from analisador.extrator_info import NanoAnalyzer
from analisador.relatorio_word import WordReport
from analisador.relatorio_excel import ExcelReport
import os

# Caminhos
PASTA_PDFS = "artigos"
SAIDA_WORD = "resultados/analise_nanoparticulas.docx"
SAIDA_EXCEL = "resultados/resumo_nanoparticulas.xlsx"

def main():
    loader = PDFLoader(PASTA_PDFS)
    artigos = loader.carregar_textos()

    analisador = NanoAnalyzer()
    resultados = []
    for nome_arquivo, texto in artigos.items():
        dados = analisador.analisar(texto)
        resultados.append({"titulo": nome_arquivo, "dados": dados})

    WordReport.gerar(SAIDA_WORD, resultados)
    ExcelReport.gerar(SAIDA_EXCEL, resultados)

if __name__ == "__main__":
    main()
