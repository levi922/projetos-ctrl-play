import tkinter as tk #importando módulo tkinter como tk

root = tk.Tk() #criando um objeto da classe TK()
root.geometry('800x600')

massage = tk.Label(root, text = 'hello world') #criando um objeto da classe Label()
massage.pack()

root.mainloop() #mostrando a janela em looping