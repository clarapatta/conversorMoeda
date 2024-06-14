#janela => 500x500
#título
#campos para selecionar as moedas de origem e destino
#botão para converter
#lista de exibição com os nomes das moedas

#importar a biblioteca que vai fazer a janela
import customtkinter

#Criar e configurar a janela 
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

#Criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("times new roman",26), text_color= "#ab1010")
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("times new roman", 14))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("times new roman", 14))

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD", "EUR", "BRL", "BTC"], font=("times new roman", 14), fg_color="#392bc1")
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD", "EUR", "BRL", "BTC"], font=("times new roman", 14), fg_color="#392bc1")

def converter_moeda():
    print("converter moeda")
botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, font=("times new roman", 20), fg_color= "#ab1010")

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD: Dólar americano","EUR: Euro","BRL: Real brasileiro","BTC: Bitcoin"]

for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda, font=("times new roman", 12))
    texto_moeda.pack()

#Colocar os elementos criados na tela
titulo.pack(padx= 10, pady=0)
texto_moeda_origem.pack(padx= 10, pady=0)
campo_moeda_origem.pack(padx= 10, pady=10)
texto_moeda_destino.pack(padx= 10, pady=0)
campo_moeda_destino.pack(padx= 10, pady=10)
botao_converter.pack(padx= 10, pady=20)
lista_moedas.pack(padx= 10, pady=10)

#rodar a janela
janela.mainloop()