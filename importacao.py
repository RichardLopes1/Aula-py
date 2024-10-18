import os
#no terminal digitem -> pip intall pandas openpyxl
import pandas as pd
os.system("cls")

#criando um dicionario com alguns dados
dados = {
    'nome':["Richard", "Weslley", "Corsi", "Lopes"],
    'idade' :[18,17,19,15],
    'Cidade':["Diadema", "São Paulo", "Santo andre","Sp"]
}

#convertendo o dicionario em um dataframe
df = pd.DataFrame(dados)

#salva o dataframe em uma planilha de excel
nome_arquivo = "panilha.xlsx"
df.to_excel(nome_arquivo, index=False)
print(f"arquivo {nome_arquivo} foi gerado")