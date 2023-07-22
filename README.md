# Meu Projeto com Interface Gráfica

Este é o meu projeto com interface gráfica que visa automatizar a união de páginas correspondentes em arquivos PDFs. O aplicativo permite a seleção de TRÊS arquivos PDFs: dois contendo informações bancárias ou seja, comprovantes de pagamentos e outro contendo recibos de pagamento dos seus empregados. As comrrespondências são baseadas no arquivo CSV que você irá subir no formato simples apenas de nomes. Delimitado por ;.  Em seguida, ele busca as páginas correspondentes no arquivo bancário, com base nos nomes das pessoas, e gera um novo arquivo PDF separado com essas páginas.. 

## Funcionalidades

- Seleção dos arquivos PDFs do banco e dos recibos de pagamento.
- Processamento dos arquivos PDFs, buscando páginas correspondentes com base nos nomes.
- Geração de um novo arquivo PDF separado contendo as páginas correspondentes. 
- Interface gráfica amigável e intuitiva.
- Une apenas 1 comprovante de pagamento para cada Recibo.
- Gera um arquivo TXT com nomes não encontrados.
- Campo onde é possível complementar o nome de saída do arquivo. Exemplo coloca competência. 

## Requisitos do Sistema

- Python 3.x
- Bibliotecas  PyPDF2 e tk (podem ser instaladas usando o arquivo requirements.txt)


## Instalação

1. Clone o repositório para a sua máquina local:


2. Acesse a pasta raiz do projeto:

   ```
   cd UNIFICA_PDF
   ```

3. Instale as dependências necessárias:

   ```
   pip install -r requirements.txt
   ```

## Como Usar

1. Execute o arquivo Unifica_PDFy:

   ```
   python Unifica_PDF.py
   ```

2. Selecione os arquivos PDFs do banco e dos recibos de pagamento utilizando os botões "Selecionar Arquivo".

3. Seleciona o arquivo CSV com as correpondencias de nomes dos empregados.  

4. Clique no  botão "Unir PDFs" para iniciar o processo de união das páginas correspondentes.

5. Aguarde o processamento e verifique a pasta de saída chamada PDF para encontrar os novos arquivos PDFs separados.
Observação: Conrrepondencias não encontradas serão enviadas ao arquivo de txt chamado pdfs_descartados.txt

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para o projeto, sinta-se à vontade para fazer um fork, criar uma branch e enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

---

Sinta-se à vontade para personalizar o conteúdo de acordo com as características e informações específicas do seu projeto. 
