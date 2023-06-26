import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
import csv
import os

class InterfaceGrafica:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("UNIFICA PDF")
        
        # Configurar eventos de arrastar
        self.janela.bind("<ButtonPress-1>", self.iniciar_arraste)
        self.janela.bind("<B1-Motion>", self.arrastar_janela)

        # Componentes da interface gráfica
        self.btn_selecionar_pdf1 = tk.Button(self.janela, text="Selecionar Banco 1", command=self.selecionar_pdf1)
        self.btn_selecionar_pdf1.pack()

        self.btn_selecionar_pdf2 = tk.Button(self.janela, text="Selecionar Banco 2", command=self.selecionar_pdf2)
        self.btn_selecionar_pdf2.pack()

        self.btn_selecionar_pdf3 = tk.Button(self.janela, text="Selecionar Recibos de Pagamentos", command=self.selecionar_pdf3)
        self.btn_selecionar_pdf3.pack()

        self.btn_selecionar_csv = tk.Button(self.janela, text="Selecionar Arquivo CSV", command=self.selecionar_arquivo_csv)
        self.btn_selecionar_csv.pack()

        self.btn_unir_pdfs = tk.Button(self.janela, text="Unir PDFs", command=self.unir_pdfs)
        self.btn_unir_pdfs.pack()

        # Variáveis para controle do arraste
        self.x_inicial = 0
        self.y_inicial = 0

        # Variáveis de controle dos arquivos carregados
        self.arquivo1_carregado = False
        self.arquivo2_carregado = False
        self.arquivo3_carregado = False
        self.arquivo_csv_carregado = False

    def iniciar_arraste(self, event):
        self.x_inicial = event.x
        self.y_inicial = event.y

    def arrastar_janela(self, event):
        desloc_x = event.x - self.x_inicial
        desloc_y = event.y - self.y_inicial
        nova_pos_x = self.janela.winfo_x() + desloc_x
        nova_pos_y = self.janela.winfo_y() + desloc_y
        self.janela.geometry(f"+{nova_pos_x}+{nova_pos_y}")

    def selecionar_pdf1(self):
        self.arquivo1 = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        self.arquivo1_carregado = True
        self.atualizar_estado_botoes()

    def selecionar_pdf2(self):
        self.arquivo2 = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        self.arquivo2_carregado = True
        self.atualizar_estado_botoes()

    def selecionar_pdf3(self):
        self.arquivo3 = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        self.arquivo3_carregado = True
        self.atualizar_estado_botoes()

    def selecionar_arquivo_csv(self):
        self.arquivo_csv = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
        self.arquivo_csv_carregado = True
        self.atualizar_estado_botoes()

    def unir_pdfs(self):
        # Verifica o arquivo CSV selecionado
        with open(self.arquivo_csv, "r") as file_csv:
            reader = csv.reader(file_csv, delimiter=";")
            for row in reader:
                palavra_chave = row[0]

                arquivo_saida = f"PDF/{palavra_chave}.pdf"

                pdf_writer = PdfWriter()

                # Verifica cada página do PDF 1
                with open(self.arquivo1, "rb") as file_pdf1:
                    pdf1 = PdfReader(file_pdf1)
                    for page in pdf1.pages:
                        texto = page.extract_text()
                        if palavra_chave in texto:
                            pdf_writer.add_page(page)

                # Verifica cada página do PDF 2
                with open(self.arquivo2, "rb") as file_pdf2:
                    pdf2 = PdfReader(file_pdf2)
                    for page in pdf2.pages:
                        texto = page.extract_text()
                        if palavra_chave in texto:
                            pdf_writer.add_page(page)

                # Verifica cada página do PDF 3
                with open(self.arquivo3, "rb") as file_pdf3:
                    pdf3 = PdfReader(file_pdf3)
                    for page in pdf3.pages:
                        texto = page.extract_text()
                        if palavra_chave in texto:
                            pdf_writer.add_page(page)

                # Verifica se o PDF resultante tem mais de 1 página
                if len(pdf_writer.pages) > 1:
                    # Cria a pasta "PDF" se não existir
                    os.makedirs("PDF", exist_ok=True)

                    # Salva o arquivo de saída com as páginas unidas
                    with open(arquivo_saida, "wb") as output_file:
                        pdf_writer.write(output_file)
                else:
                    # Salva o nome da linha do CSV em um arquivo de texto
                    with open("pdfs_descartados.txt", "a") as txt_file:
                        txt_file.write(f"Empregado encontrado: {palavra_chave}\n")

        print("Os PDFs foram unidos e salvos individualmente com base no arquivo CSV.")
        
    def atualizar_estado_botoes(self):
        if self.arquivo1_carregado:
            self.btn_selecionar_pdf1.configure(bg='green')
        if self.arquivo2_carregado:
            self.btn_selecionar_pdf2.configure(bg='green')
        if self.arquivo3_carregado:
            self.btn_selecionar_pdf3.configure(bg='green')
        if self.arquivo_csv_carregado:
            self.btn_selecionar_csv.configure(bg='green')

    def iniciar(self):
        self.janela.mainloop()

# interface gráfica
interface = InterfaceGrafica()
interface.iniciar()
