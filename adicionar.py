from tkinter import *

root = Tk()

class new_window:
    def __init__(self, master=None):
        self.root = root
        self.window()
        self.labels()
        self.entrys()
        root.mainloop()

    def window(self):
        root.title('Controle de Estoque')
        root.geometry("600x350")
    def labels(self):
        self.product = ''
        self.marca = ''
        self.loc_estoque = ''
        self.estoque_min = ''
        self.estoque_max = ''
        self.peso_kg = ''
        self.valor_venda = ''
        self.valor_custo = ''
        self.tamanho_produto = ''
        self.origem = ''
        self.situação = ''
        self.tipo = ''
        self.fornecedor = ''
        self.estoque_inicial = ''

        self.lblProduct = Label(root, text='Produto')
        self.lblProduct.grid(row=0, column=0)

        self.lblmarca = Label(root, text='Marca')
        self.lblmarca.grid(row=0, column=1)

        self.lblLocalest = Label(root, text='Local no Estoque')
        self.lblLocalest.grid(row=0, column=2)

        self.lblestoquemin = Label(root, text='Estoque minímo')
        self.lblestoquemin.grid(row=0, column=3)

        self.lblestoquemax = Label(root, text='Estoque maxímo')
        self.lblestoquemax.grid(row=0, column=4)

        self.lblPeso = Label(root, text='Peso (Kg)')
        self.lblPeso.grid(row=0, column=5)

        self.lblv_venda = Label(root, text='Valor de venda')
        self.lblv_venda.grid(row=2, column=0)

        self.lblv_custo = Label(root, text='Valor de custo')
        self.lblv_custo.grid(row=2, column=1)

        self.lbltam_produto = Label(root, text='Tamanho do produto')
        self.lbltam_produto.grid(row=2, column=2)

        self.lblorigem = Label(root, text='Origem')
        self.lblorigem.grid(row=2, column=3)

        self.lblsituacao = Label(root, text='Situação')
        self.lblsituacao.grid(row=2, column=4)

        self.lbltipo = Label(root, text='Tipo')
        self.lbltipo.grid(row=2, column=5)

        self.lblfornecedor = Label(root, text='Fornecedor')
        self.lblfornecedor.grid(row=4, column=0)

        self.lblesto_inicial = Label(root, text='Estoque inicial')
        self.lblesto_inicial.grid(row=4, column=1)

        self.listProdutos = Listbox(root)
        self.scrollProdutos = Scrollbar(root)

    def entrys(self):
        self.entryProduct = Entry(root, textvariable=self.product)
        self.entryProduct.grid(row=1, column=0, padx=20, pady=10)

        self.entryMarca = Entry(root, textvariable=self.marca)
        self.entryMarca.grid(row=1, column=1, padx=20, pady=10)

        self.entrylocalEstoque = Entry(root, textvariable=self.loc_estoque)
        self.entrylocalEstoque.grid(row=1, column=2, padx=20, pady=10)

        self.entryestoqueMin = Entry(root, textvariable=self.estoque_min)
        self.entryestoqueMin.grid(row=1, column=3, padx=20, pady=10)

        self.entryestoque_max = Entry(root, textvariable=self.estoque_max)
        self.entryestoque_max.grid(row=1, column=4, padx=20, pady=10)

        self.entryPeso = Entry(root, textvariable=self.peso_kg)
        self.entryPeso.grid(row=1, column=5, padx=20, pady=10)

        self.entryv_venda = Entry(root, textvariable=self.valor_venda)
        self.entryv_venda.grid(row=3, column=0, padx=20, pady=10)

        self.entryv_custo = Entry(root, textvariable=self.valor_custo)
        self.entryv_custo.grid(row=3, column=1, padx=20, pady=10)

        self.entrytam_produto = Entry(root, textvariable=self.tamanho_produto)
        self.entrytam_produto.grid(row=3, column=2, padx=20, pady=10)

        self.entryorigem = Entry(root, textvariable=self.origem)
        self.entryorigem.grid(row=3, column=3, padx=20, pady=10)

        self.entrySituacao = Entry(root, textvariable=self.situação)
        self.entrySituacao.grid(row=3, column=4, padx=20, pady=10)

        self.entryTipo = Entry(root, textvariable=self.tipo)
        self.entryTipo.grid(row=3, column=5, padx=20, pady=10)

        self.entryFornecedor = Entry(root, textvariable=self.fornecedor)
        self.entryFornecedor.grid(row=5, column=0, padx=20, pady=10)

        self.entryEstoInicial = Entry(root, textvariable=self.estoque_inicial)
        self.entryEstoInicial.grid(row=5, column=1, padx=20, pady=10)

        self.listProdutos.grid(row=6, column=0, rowspan=10)
        self.scrollProdutos.grid(row=6, column=1, rowspan=10)

        self.listProdutos.configure(yscrollcommand=self.scrollProdutos.set)
        self.scrollProdutos.configure(command=self.listProdutos.yview)

new_window()
