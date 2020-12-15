from tkinter import *
# from adicionar import new_window
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

        # self.pesquisar = Frame(root, width=200, height=50, background="Red")
        # self.pesquisar.grid(row=0, column=1)

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

    # def new_window(self):
    #     Newwindow = Toplevel(self.root)
    #     Newwindow.geometry("600x450")

    #     janela_cadastro = Frame(Newwindow, width=600, height=225, background='Blue')
    #     janela_cadastro.grid(row=0, column=0)

    #     product = ''
    #     marca = ''
    #     loc_estoque = ''
    #     estoque_min = ''
    #     estoque_max = ''
    #     peso_kg = ''
    #     valor_venda = ''
    #     valor_custo = ''
    #     tamanho_produto = ''
    #     origem = ''
    #     classificação = ''
    #     situação = ''
    #     tipo = ''
    #     fornecedor = ''
    #     estoque_inicial = ''

    #     lblProduct = Label(janela_cadastro, text='Produto')
    #     lblProduct.place(x=30, y=5)

    #     lblmarca = Label(janela_cadastro, text='Marca')
    #     lblmarca.place(x=130, y=5)

    #     lblLocalest = Label(janela_cadastro, text='Local no Estoque')
    #     lblLocalest.place(x=230, y=5)

    #     lblestoquemin = Label(janela_cadastro, text='Estoque minímo')
    #     lblestoquemin.place(x=390, y=5)

    #     lblestoquemax = Label(janela_cadastro, text='Estoque maxímo')
    #     lblestoquemax.place(x=510, y=5)

        # lblPeso = Label(Newwindow, text='Peso (Kg)')
        # lblPeso.grid(row=0, column=5)

        # lblv_venda = Label(Newwindow, text='Valor de venda')
        # lblv_venda.grid(row=2, column=0)

        # lblv_custo = Label(Newwindow, text='Valor de custo')
        # lblv_custo.grid(row=2, column=1)

        # lbltam_produto = Label(Newwindow, text='Tamanho do produto')
        # lbltam_produto.grid(row=2, column=2)

        # lblorigem = Label(Newwindow, text='Origem')
        # lblorigem.grid(row=2, column=3)

        # lblsituacao = Label(Newwindow, text='Situação')
        # lblsituacao.grid(row=2, column=4)

        # lbltipo = Label(Newwindow, text='Tipo')
        # lbltipo.grid(row=2, column=5)

        # lblfornecedor = Label(Newwindow, text='Fornecedor')
        # lblfornecedor.grid(row=4, column=0)

        # lblesto_inicial = Label(Newwindow, text='Estoque inicial')
        # lblesto_inicial.grid(row=4, column=1)

        # listProdutos = Listbox(Newwindow)
        # scrollProdutos = Scrollbar(Newwindow)

        # entryProduct = Entry(janela_cadastro, textvariable=product)
        # entryProduct.place(x=10, y=50)

        # entryMarca = Entry(janela_cadastro, textvariable=marca)
        # entryMarca.place(x=100, y=50)

        # entrylocalEstoque = Entry(janela_cadastro, textvariable=loc_estoque)
        # entrylocalEstoque.place(x=200, y=50)

        # entryestoqueMin = Entry(janela_cadastro, textvariable=estoque_min)
        # entryestoqueMin.place(x=300, y=50)

        # entryestoque_max = Entry(janela_cadastro, textvariable=estoque_max)
        # entryestoque_max.place(x=400, y=50)

        # entryPeso = Entry(Newwindow, textvariable=peso_kg)
        # entryPeso.grid(row=1, column=5, padx=20, pady=10)

        # entryv_venda = Entry(Newwindow, textvariable=valor_venda)
        # entryv_venda.grid(row=3, column=0, padx=20, pady=10)

        # entryv_custo = Entry(Newwindow, textvariable=valor_custo)
        # entryv_custo.grid(row=3, column=1, padx=20, pady=10)

        # entrytam_produto = Entry(Newwindow, textvariable=tamanho_produto)
        # entrytam_produto.grid(row=3, column=2, padx=20, pady=10)

        # entryorigem = Entry(Newwindow, textvariable=origem)
        # entryorigem.grid(row=3, column=3, padx=20, pady=10)

        # entrySituacao = Entry(Newwindow, textvariable=situação)
        # entrySituacao.grid(row=3, column=4, padx=20, pady=10)

        # entryTipo = Entry(Newwindow, textvariable=tipo)
        # entryTipo.grid(row=3, column=5, padx=20, pady=10)

        # entryFornecedor = Entry(Newwindow, textvariable=fornecedor)
        # entryFornecedor.grid(row=5, column=0, padx=20, pady=10)

        # entryEstoInicial = Entry(Newwindow, textvariable=estoque_inicial)
        # entryEstoInicial.grid(row=5, column=1, padx=20, pady=10)
        
Application(root)
