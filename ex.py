import os
#no terminal digitem -> pip intall pandas openpyxl
import pandas as pd
os.system("cls")

def menu():
    while True:
        print('''
              0-SAIR
              1-CADASTRAR
              2-LISTAR/EXPORTAR
              ''')
        
        escolha = input ("Escolha:")

        match escolha:
            case "0":
                print("Saindo.....")
                break

            case "1":
                print("Cadatrar")
                cadastro = input("cadastre uma tabela:")
        
menu()