# Scraping PDF (GetPDF)

## Descrição do Projeto

Este projeto fornece uma classe para extração de tabelas de arquivos PDF utilizando camelot-py e pypdfium2.

## Pré-requisitos

- Python 3.8+
- Pip (Gerenciador de pacotes Python)

## Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/gladson/scraping-pdf.git
cd scraping-pdf
```

### 2. Criar Ambiente Virtual

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

#### Dependências Principais

- camelot-py
- pypdfium2
- pandas

### Criação do arquivo requirements.txt

Se ainda não tiver um, crie um arquivo `requirements.txt` com o seguinte conteúdo:

```
camelot-py
pypdfium2
pandas
```

## Problemas Comuns de Instalação

### No Linux

Pode ser necessário instalar dependências adicionais:

```bash
# Para Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y libpoppler-dev python3-dev
sudo apt-get install -y tesseract-ocr libtesseract-dev
```

### No Windows

#### Preparação do Ambiente

1. **Python 64-bit**

   - Baixe o Python 64-bit no site oficial (https://www.python.org/downloads/)
   - Marque a opção "Adicionar Python ao PATH" durante a instalação

2. **Dependências do Sistema**

   - **Visual C++ Build Tools**
     - Baixe e instale o "Build Tools for Visual Studio"
     - Link: https://visualstudio.microsoft.com/visual-cpp-build-tools/
     - Durante a instalação, selecione "Ferramentas de Compilação C++"

3. **Dependências Específicas**

   ```bash
   # Atualizar pip
   python -m pip install --upgrade pip

   # Instalar dependências de sistema
   pip install wheel
   pip install setuptools
   ```

4. **Resolução de Problemas Comuns**

   - Se encontrar erros de compilação, use:

     ```bash
     pip install --upgrade pip setuptools wheel
     ```

   - Para camelot-py e pypdfium2, pode ser necessário:
     ```bash
     pip install opencv-python-headless
     pip install poppler-utils
     ```

5. **Instalação de Poppler** (opcional, mas recomendado)
   - Baixe o Poppler para Windows:
     - Acesse: https://github.com/oschwartz10612/poppler-windows/releases/
     - Baixe a versão mais recente
     - Extraia para um diretório (ex: C:\poppler)
   - Adicione o diretório bin ao PATH do sistema:
     - Painel de Controle > Sistema > Configurações Avançadas do Sistema
     - Variáveis de Ambiente > PATH > Novo
     - Adicione o caminho para a pasta bin do Poppler

#### Dicas Adicionais

- Use sempre o Prompt de Comando ou PowerShell como Administrador
- Verifique a compatibilidade das versões de Python e bibliotecas
- Em caso de erros persistentes, considere usar Anaconda ou ambiente virtual conda

## Uso Básico

### Exemplo de Código

```python
from get_pdf import GetPDF

# Caminho para seu arquivo PDF
pdf_path = 'seu_arquivo.pdf'

# Criar instância do extrator
pdf_extractor = GetPDF(pdf_path)

# Extrair tabelas
tables = pdf_extractor.extract_tables(
    pages='all',  # Todas as páginas
    flavor='lattice'  # Detectar tabelas com linhas
)

# Converter tabelas para DataFrames
dataframes = pdf_extractor.convert_tables_to_dataframes()

# Salvar tabelas em CSV
pdf_extractor.save_tables_to_csv()

# Gerar pré-visualização da primeira página
pdf_extractor.preview_pdf_page()
```

## Métodos Principais

### `extract_tables(pages='all', flavor='lattice')`

- `pages`: Páginas para extrair tabelas
  - `'all'`: Todas as páginas
  - `'1,3,4'`: Páginas específicas
- `flavor`: Método de detecção de tabelas
  - `'lattice'`: Para tabelas com linhas claras
  - `'stream'`: Para tabelas sem linhas definidas

### `convert_tables_to_dataframes()`

- Converte tabelas extraídas para pandas DataFrames

### `save_tables_to_csv(output_dir='./output')`

- Salva tabelas extraídas como arquivos CSV
- Permite especificar diretório de saída

### `preview_pdf_page(page_number=0, output_path='preview.png')`

- Gera imagem de pré-visualização de página específica

## Solução de Problemas

### Erros Comuns

- Verificar se o PDF tem tabelas bem definidas
- Ajustar `flavor` entre `'lattice'` e `'stream'`
- Garantir que o PDF não está protegido ou criptografado

### Logs e Depuração

- Verifique as mensagens de erro no console
- Use parâmetros como `pages` para extrair tabelas específicas

## Limitações

- Funciona melhor com PDFs estruturados
- Pode não funcionar perfeitamente com PDFs digitalizados ou com layout complexo

## Contribuição

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas alterações
4. Abra um Pull Request

## Licença

[MIT](https://github.com/gladson/scraping-pdf/blob/main/LICENSE)
