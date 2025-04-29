import fitz  # PyMuPDF
import pandas as pd
import re

# Abrir o PDF
doc = fitz.open("seuarq.pdf")
text = ""
for page in doc:
    text += page.get_text()

# Encontrar linhas com padrão "número. palavra - tradução"
linhas = re.findall(r"\d+\.\s+.+?-\s+.+", text)

palavras_portugues = []

# Extrair só as traduções em português
for linha in linhas:
    try:
        partes = linha.split('-')
        traducao = partes[1].strip()
        palavras_portugues.append(traducao)
    except IndexError:
        continue

# Criar planilha com coluna para tradução
df = pd.DataFrame({
    'Português': palavras_portugues,
    'Tradução para o inglês': [''] * len(palavras_portugues)
})

# Salvar a planilha
df.to_excel("planilha_traducoes.xlsx", index=False)
print("✅ Planilha criada com sucesso!")
