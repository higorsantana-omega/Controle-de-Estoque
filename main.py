from tkinter import *
from novo_produto import vp_start_gui

root = Tk()

class Application:
    def __init__(self, master=None):
        self.root = root
        self.window()
        self.frames()
        self.buttons()
        root.mainloop()

    def window(self):
        root.title('Controle de Estoque')
        root.geometry("600x350")

    def frames(self):
        self.botoes = Frame(self.root, width=600, height=50)
        self.botoes.grid(row=0, column=0)

        self.listbox_ = Frame(self.root, width=600, height=300)
        self.listbox_.grid(row=2, column=0)

    def buttons(self):
        self.adicionar = Button(self.botoes, text='Adicionar', width=12, height=2, command=vp_start_gui)
        self.adicionar.place(x=10, y=5)

        self.importar = Button(self.botoes, text='Importar', width=12, height=2)
        self.importar.place(x=110, y=5)

        self.excluir = Button(self.botoes, text='Excluir', width=12, height=2)
        self.excluir.place(x=210, y=5) 

        self.listProdutos = Listbox(self.listbox_, width=96, height=18)
        self.scrollProdutos = Scrollbar(self.listbox_)
        self.listProdutos.grid(row=0, column=0, rowspan=10)
        self.scrollProdutos.grid(row=0, column=1, rowspan=10)

        self.listProdutos.configure(yscrollcommand=self.scrollProdutos.set)
        self.scrollProdutos.configure(command=self.listProdutos.yview)
        
Application(root)
