import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import novo_produto_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    novo_produto_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    novo_produto_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Times New Roman} -size 14 -weight bold"

        top.geometry("600x500+436+89")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Novo produto")
        top.configure(background="#d9d9d9")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.65, rely=0.14,height=20, relwidth=0.14)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.033, rely=0.14,height=20, relwidth=0.583)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.033, rely=0.1, height=20, width=104)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Nome do produto''')

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.033, rely=0.24,height=20, relwidth=0.24)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.65, rely=0.1, height=20, width=39)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''ID''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.033, rely=0.2, height=20, width=44)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Marca''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.3, rely=0.2, height=20, width=50)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Unidade''')

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.3, rely=0.24,height=20, relwidth=0.14)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.033, rely=0.3, height=20, width=130)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Localização no estoque''')

        self.Entry5 = tk.Entry(top)
        self.Entry5.place(relx=0.033, rely=0.34,height=20, relwidth=0.24)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.3, rely=0.3, height=21, width=93)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Estoque mínimo''')

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.567, rely=0.3, height=21, width=94)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Estoque máximo''')

        self.Entry5_1 = tk.Entry(top)
        self.Entry5_1.place(relx=0.3, rely=0.34,height=20, relwidth=0.24)
        self.Entry5_1.configure(background="white")
        self.Entry5_1.configure(disabledforeground="#a3a3a3")
        self.Entry5_1.configure(font="TkFixedFont")
        self.Entry5_1.configure(foreground="#000000")
        self.Entry5_1.configure(highlightbackground="#d9d9d9")
        self.Entry5_1.configure(highlightcolor="black")
        self.Entry5_1.configure(insertbackground="black")
        self.Entry5_1.configure(selectbackground="#c4c4c4")
        self.Entry5_1.configure(selectforeground="black")

        self.Entry5_2 = tk.Entry(top)
        self.Entry5_2.place(relx=0.567, rely=0.34,height=20, relwidth=0.24)
        self.Entry5_2.configure(background="white")
        self.Entry5_2.configure(disabledforeground="#a3a3a3")
        self.Entry5_2.configure(font="TkFixedFont")
        self.Entry5_2.configure(foreground="#000000")
        self.Entry5_2.configure(highlightbackground="#d9d9d9")
        self.Entry5_2.configure(highlightcolor="black")
        self.Entry5_2.configure(insertbackground="black")
        self.Entry5_2.configure(selectbackground="#c4c4c4")
        self.Entry5_2.configure(selectforeground="black")

        self.Entry5_3 = tk.Entry(top)
        self.Entry5_3.place(relx=0.833, rely=0.34,height=20, relwidth=0.123)
        self.Entry5_3.configure(background="white")
        self.Entry5_3.configure(disabledforeground="#a3a3a3")
        self.Entry5_3.configure(font="TkFixedFont")
        self.Entry5_3.configure(foreground="#000000")
        self.Entry5_3.configure(highlightbackground="#d9d9d9")
        self.Entry5_3.configure(highlightcolor="black")
        self.Entry5_3.configure(insertbackground="black")
        self.Entry5_3.configure(selectbackground="#c4c4c4")
        self.Entry5_3.configure(selectforeground="black")

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.833, rely=0.3, height=20, width=68)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Peso em Kg''')

        self.Entry6 = tk.Entry(top)
        self.Entry6.place(relx=0.033, rely=0.44,height=20, relwidth=0.24)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")

        self.Entry7 = tk.Entry(top)
        self.Entry7.place(relx=0.3, rely=0.44,height=20, relwidth=0.24)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")

        self.Label9 = tk.Label(top)
        self.Label9.place(relx=0.033, rely=0.4, height=20, width=84)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Valor de venda''')

        self.Label10 = tk.Label(top)
        self.Label10.place(relx=0.3, rely=0.4, height=20, width=81)
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Valor de custo''')

        self.Label11 = tk.Label(top)
        self.Label11.place(relx=0.033, rely=0.5, height=20, width=120)
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''Tamanho do produto''')

        self.Label12 = tk.Label(top)
        self.Label12.place(relx=0.3, rely=0.5, height=21, width=46)
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''Origem''')

        self.Entry8 = tk.Entry(top)
        self.Entry8.place(relx=0.033, rely=0.54,height=20, relwidth=0.24)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(insertbackground="black")

        self.Entry9 = tk.Entry(top)
        self.Entry9.place(relx=0.3, rely=0.54,height=20, relwidth=0.24)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(insertbackground="black")

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.567, rely=0.54, relheight=0.144
                , relwidth=0.24)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")

        self.Label13 = tk.Label(top)
        self.Label13.place(relx=0.567, rely=0.5, height=20, width=74)
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''Classificação''')

        self.Label14 = tk.Label(top)
        self.Label14.place(relx=0.033, rely=0.72, height=20, width=51)
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''Situação''')

        self.Label15 = tk.Label(top)
        self.Label15.place(relx=0.183, rely=0.72, height=20, width=30)
        self.Label15.configure(background="#d9d9d9")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''Tipo''')

        self.Label16 = tk.Label(top)
        self.Label16.place(relx=0.417, rely=0.72, height=20, width=66)
        self.Label16.configure(background="#d9d9d9")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(text='''Fornecedor''')

        self.Label17 = tk.Label(top)
        self.Label17.place(relx=0.667, rely=0.72, height=21, width=82)
        self.Label17.configure(background="#d9d9d9")
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(text='''Estoque inicial''')

        self.Listbox2 = tk.Listbox(top)
        self.Listbox2.place(relx=0.033, rely=0.76, relheight=0.064
                , relwidth=0.123)
        self.Listbox2.configure(background="white")
        self.Listbox2.configure(disabledforeground="#a3a3a3")
        self.Listbox2.configure(font="TkFixedFont")
        self.Listbox2.configure(foreground="#000000")

        self.Listbox3 = tk.Listbox(top)
        self.Listbox3.place(relx=0.167, rely=0.76, relheight=0.064
                , relwidth=0.24)
        self.Listbox3.configure(background="white")
        self.Listbox3.configure(disabledforeground="#a3a3a3")
        self.Listbox3.configure(font="TkFixedFont")
        self.Listbox3.configure(foreground="#000000")

        self.Entry10 = tk.Entry(top)
        self.Entry10.place(relx=0.417, rely=0.76,height=20, relwidth=0.24)
        self.Entry10.configure(background="white")
        self.Entry10.configure(disabledforeground="#a3a3a3")
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.configure(foreground="#000000")
        self.Entry10.configure(insertbackground="black")

        self.Entry11 = tk.Entry(top)
        self.Entry11.place(relx=0.667, rely=0.76,height=20, relwidth=0.24)
        self.Entry11.configure(background="white")
        self.Entry11.configure(disabledforeground="#a3a3a3")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(foreground="#000000")
        self.Entry11.configure(insertbackground="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.033, rely=0.94, height=24, width=90)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.2, rely=0.94, height=24, width=90)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="sunken")
        self.Button2.configure(state='active')
        self.Button2.configure(text='''Button''')

        self.Label18 = tk.Label(top)
        self.Label18.place(relx=0.183, rely=0.02, height=41, width=378)
        self.Label18.configure(background="#d9d9d9")
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(font=font9)
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(text='''NOVO PRODUTO''')

if __name__ == '__main__':
    vp_start_gui()





