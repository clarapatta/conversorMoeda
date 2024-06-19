#janela => 500x500
#título
#campos para selecionar as moedas de origem e destino
#botão para converter
#lista de exibição com os nomes das moedas

#importar a biblioteca que vai fazer a janela
import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotaçao_moeda

#Criar e configurar a janela 
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("400x600")
janela.title("Conversor de Moedas")
janela.iconbitmap("moedas.ico")

dic_conversoes_disponiveis = conversoes_disponiveis()

#Criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("times new roman",26), text_color= "#ab1010")

texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("times new roman", 14))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("times new roman", 14))

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino, font=("times new roman", 14), fg_color="#392bc1")

campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"], font=("times new roman", 14), fg_color="#392bc1") # type: ignore

def converter_moeda():
   moeda_origem = campo_moeda_origem.get()
   moeda_destino = campo_moeda_destino.get()
   if moeda_origem and moeda_destino:
       cotaçao = pegar_cotaçao_moeda(moeda_origem, moeda_destino)
       texto_cotaçao_moeda.configure(text=f"1 {moeda_origem} = {cotaçao}{moeda_destino}")
   
botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, font=("times new roman", 20), fg_color= "#ab1010")

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotaçao_moeda = customtkinter.CTkLabel(janela, text="", fg_color= "#392bc1", font=("times new roman", 14), text_color= "#fcfcf9")

moedas_disponiveis = nomes_moedas()

for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}", font=("times new roman", 12))
    texto_moeda.pack()

#Colocar os elementos criados na tela
titulo.pack(padx= 10, pady=0)
texto_moeda_origem.pack(padx= 10, pady=0)
campo_moeda_origem.pack(padx= 10, pady=10)
texto_moeda_destino.pack(padx= 10, pady=0)
campo_moeda_destino.pack(padx= 10, pady=10)
botao_converter.pack(padx= 10, pady=20)
texto_cotaçao_moeda.pack(padx= 10, pady= 10)
lista_moedas.pack(padx= 10, pady=10)


#rodar a janela
janela.mainloop()
