import tkinter
import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Tela:
    def __init__(self):
        # Iniciar Tela
        self.tela = Tk()
        self.tela.geometry("400x400")
        self.tela.title("Conversor de Moedas em Tempo Real")
        self.tela.configure(background="#484f60")

        self.style = ttk.Style(self.tela)
        self.style.theme_use("clam")

        #Texto Topo
        texto_selecione = Label(self.tela, text="Selecione as moedas", width=20, font=('Arial 16 bold'), background="#484f60", fg="#FFFFFF")
        texto_selecione.place(x=70, y=10)

        # COMBOBOX
        self.moeda_selecionada_base = tkinter.StringVar()
        self.combo_origem = ttk.Combobox(self.tela, textvariable=self.moeda_selecionada_base, width=10, justify=CENTER,font=('Ivy 12 bold'))
        self.combo_origem.place(x=70, y=65)

        self.moeda_selecionada_alvo = tkinter.StringVar()
        self.combo_alvo = ttk.Combobox(self.tela, textvariable=self.moeda_selecionada_alvo, width=10, justify=CENTER,font=('Ivy 12 bold'))
        self.combo_alvo.place(x=230, y=65)

        # Campo de entrada para a quantidade de dinheiro
        self.entrada_quantidade = Entry(self.tela, width=22,justify=CENTER, font=('Ivy 12 bold'), relief=SOLID)
        self.entrada_quantidade.place(x=100, y=120)

        # Rótulo para exibir o resultado da conversão
        self.rotulo_quantidade = Label(self.tela, text='', width=17, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg='#ffffff', fg="#333333")
        self.rotulo_quantidade.place(x=100, y=270)

        self.botao_converter = Button(self.tela, text="Converter", width=19,padx=5, height=1, bg='#ffffff', fg="#FFFFFF",  font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE, command=self.converter)
        self.botao_converter.place(x=100, y=180)
        self.botao_converter.configure(background="#444466")

        self.obter_nome()
        self.tela.mainloop()

    #Função para trazer a Taxa de conversão da moeda base para moeda alvo
    def obter_taxa(self, moeda_base, moeda_alvo):
        url = f"https://api.exchangerate-api.com/v4/latest/{moeda_base}"
        response = requests.get(url)
        valor_api = response.json()
        taxa = valor_api['rates'][moeda_alvo]
        return taxa

    #Função para Trazer os nomes das moedas da url, e listar nos dois ComboBox's 
    def obter_nome(self):
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        nome_api = response.json()
        self.dict_nomes = nome_api['rates']
        self.combo_origem['values'] = list(self.dict_nomes.keys())
        self.combo_alvo['values'] = list(self.dict_nomes.keys())

    #Função que converte as moedas e seta o valor do campo de resultado para o resultado
    def converter(self):
        moeda_base = self.moeda_selecionada_base.get()
        moeda_alvo = self.moeda_selecionada_alvo.get()

        try:
            quantidade = float(self.entrada_quantidade.get())
        except ValueError as e: 
            messagebox.showerror("Erro", f"Digite um valor numérico válido. \nDetalhes: {e}")

            messagebox.showinfo("Informação", "Certifique-se de inserir um número válido para a quantidade.")
            return
        
        taxa = self.obter_taxa(moeda_base, moeda_alvo)
        resultado = quantidade * taxa

        self.rotulo_quantidade.config(text=f"{resultado:.2f} {moeda_alvo}")


if __name__ == "__main__":
    Tela()
