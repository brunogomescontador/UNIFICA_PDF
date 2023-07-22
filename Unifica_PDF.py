import tkinter as tk
from tkinter import filedialog , messagebox
from PyPDF2 import PdfReader, PdfWriter
import csv
import os
import logging

# Configurar o logger
logging.basicConfig(filename='meuapp.log', level=logging.ERROR)

class InterfaceGrafica:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("GAP SSMA")

        # Configurar eventos de arrastar
        self.janela.bind("<ButtonPress-1>", self.iniciar_arraste)
        self.janela.bind("<B1-Motion>", self.arrastar_janela)

    # Frame para a seleção de arquivos
        self.frame_selecao = tk.Frame(self.janela)
        self.frame_selecao.pack(pady=10)

        self.instrucoes = tk.Label(self.frame_selecao, text="Por favor, selecione os arquivos PDF e CSV que deseja unificar.")
        self.instrucoes.pack()

        # Frame para Banco 1
        self.frame_banco1 = tk.Frame(self.frame_selecao)
        self.frame_banco1.pack(fill='x')
        self.btn_selecionar_pdf1 = tk.Button(self.frame_banco1, text="Selecionar Banco 1", command=self.selecionar_pdf1)
        self.btn_selecionar_pdf1.pack(side='left')
        self.nome_pdf1 = tk.Label(self.frame_banco1, text="")
        self.nome_pdf1.pack(side='left')

        # Frame para Banco 2
        self.frame_banco2 = tk.Frame(self.frame_selecao)
        self.frame_banco2.pack(fill='x')
        self.btn_selecionar_pdf2 = tk.Button(self.frame_banco2, text="Selecionar Banco 2", command=self.selecionar_pdf2)
        self.btn_selecionar_pdf2.pack(side='left')
        self.nome_pdf2 = tk.Label(self.frame_banco2, text="")
        self.nome_pdf2.pack(side='left')

        # Frame para Folha de Pagamento
        self.frame_folha_pagamento = tk.Frame(self.frame_selecao)
        self.frame_folha_pagamento.pack(fill='x')
        self.btn_selecionar_pdf3 = tk.Button(self.frame_folha_pagamento, text="Selecionar Folha de Pagamento", command=self.selecionar_pdf3)
        self.btn_selecionar_pdf3.pack(side='left')
        self.nome_pdf3 = tk.Label(self.frame_folha_pagamento, text="")
        self.nome_pdf3.pack(side='left')

        # Frame para CSV
        self.frame_csv = tk.Frame(self.frame_selecao)
        self.frame_csv.pack(fill='x')
        self.btn_selecionar_csv = tk.Button(self.frame_csv, text="Selecionar CSV", command=self.selecionar_csv)
        self.btn_selecionar_csv.pack(side='left')
        self.nome_csv = tk.Label(self.frame_csv, text="")
        self.nome_csv.pack(side='left')

        self.entry_palavra_chave = tk.Entry(self.janela)
        self.entry_palavra_chave.pack()

        # Frame para a unificação
        self.frame_unificacao = tk.Frame(self.janela)
        self.frame_unificacao.pack(pady=10)

        self.btn_unificar = tk.Button(self.frame_unificacao, text="Unificar PDFs", command=self.unificar_pdfs)
        self.btn_unificar.pack()
        caminho_absoluto = os.path.abspath(os.getcwd())       
        caminho_img = os.path.join(caminho_absoluto, "img", "loading.gif")
        # Label para o GIF de carregamento
        self.loading_gif = tk.PhotoImage(file=caminho_img)
        self.loading_label = tk.Label(self.frame_unificacao, image=self.loading_gif)
        self.loading_label.pack()
        self.loading_label.pack_forget()  # Oculta o label no início

        
        # Variáveis para controle do arraste
        self.x_inicial = 0
        self.y_inicial = 0

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
        self.nome_pdf1.config(text=f"Arquivo selecionado: {os.path.basename(self.arquivo1)}")
        self.btn_selecionar_pdf1.config(bg='green')

    def selecionar_pdf2(self):
        self.arquivo2 = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        self.nome_pdf2.config(text=f"Arquivo selecionado: {os.path.basename(self.arquivo2)}")
        self.btn_selecionar_pdf2.config(bg='green')

    def selecionar_pdf3(self):
        self.arquivo3 = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        self.nome_pdf3.config(text=f"Arquivo selecionado: {os.path.basename(self.arquivo3)}")
        self.btn_selecionar_pdf3.config(bg='green')

    def selecionar_csv(self):
        self.arquivo_csv = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
        self.nome_csv.config(text=f"Arquivo selecionado: {os.path.basename(self.arquivo_csv)}")
        self.btn_selecionar_csv.config(bg='green')

    def unificar_pdfs(self):
        self.btn_unificar.config(bg='yellow')  # Muda a cor do botão para amarelo
        self.loading_label.pack()  # Mostra o label de carregamento
        self.janela.after(1000, self.realizar_unificacao)  # Agendar a unificação para começar após 100ms

    def realizar_unificacao(self):
        try:
            # Verifica o arquivo CSV selecionado
            with open(self.arquivo_csv, "r") as file_csv:
                reader = csv.reader(file_csv, delimiter=";")
                for row in reader:
                    palavra_chave = row[0]
                    # Cria a pasta "PDF" no mesmo diretório do script se não existir
                    dir_path = os.path.dirname(os.path.realpath(__file__))
                    os.makedirs(os.path.join(dir_path, "PDF"), exist_ok=True)

                    complemento = self.entry_palavra_chave.get()

                    if complemento:  # Se a entrada não estiver vazia
                        arquivo_saida = os.path.join(dir_path, f"PDF/{complemento}{palavra_chave}.pdf")
                    else:  # Se a entrada estiver vazia
                        arquivo_saida = os.path.join(dir_path, f"PDF/{palavra_chave}.pdf")
                        # Aqui você pode adicionar o código para lidar com a situação em que nenhuma palavra-chave foi inserida
                            
                    #arquivo_saida = os.path.join(dir_path, f"PDF/{palavra_chave}.pdf")

                    pdf_writer = PdfWriter()
                    if not hasattr(self, 'arquivo1') or not self.arquivo1:
                        pass
                    else:
                        # Verifica cada página do PDF 1
                        with open(self.arquivo1, "rb") as file_pdf1:
                            pdf1 = PdfReader(file_pdf1)
                            for page in pdf1.pages:
                                texto = page.extract_text()
                                if palavra_chave in texto:
                                    pdf_writer.add_page(page)

                    # Verifica cada página do PDF 2
                    if not hasattr(self, 'arquivo2') or not self.arquivo2:
                        pass
                    else:
                        with open(self.arquivo2, "rb") as file_pdf2:
                            pdf2 = PdfReader(file_pdf2)
                            for page in pdf2.pages:
                                texto = page.extract_text()
                                if palavra_chave in texto:
                                    pdf_writer.add_page(page)
                    if not hasattr(self, 'arquivo1') or not self.arquivo1:
                       messagebox.showerror("Erro", "Por favor, selecione um arquivo de Folha.")
                    else:
                        # Verifica cada página do PDF 3
                        with open(self.arquivo3, "rb") as file_pdf3:
                            pdf3 = PdfReader(file_pdf3)
                            for page in pdf3.pages:
                                texto = page.extract_text()
                                if palavra_chave in texto:
                                    pdf_writer.add_page(page)

                    # Verifica se o PDF resultante tem mais de 1 página
                    if len(pdf_writer.pages) > 1:
                        # Salva o arquivo de saída com as páginas unidas
                        with open(arquivo_saida, "wb") as output_file:
                            pdf_writer.write(output_file)
                    else:
                        # Salva o nome da linha do CSV em um arquivo de texto
                        with open(os.path.join(dir_path, "pdfs_descartados.txt"), "a") as txt_file:
                            txt_file.write(f"Empregado não encontrado: {palavra_chave}\n")

        except Exception as e:
            logging.exception("ERRO!", "A unificação dos PDFs não funcionou")

        finally:
            self.loading_label.pack_forget()  # Oculta o label de carregamento quando a unificação é concluída
            self.btn_unificar.config(bg='green')  # Muda a cor do botão de volta ao padrão
            #messagebox.showinfo("Operação concluída", "A unificação dos PDFs foi concluída com sucesso.")

    def executar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    InterfaceGrafica().executar()
