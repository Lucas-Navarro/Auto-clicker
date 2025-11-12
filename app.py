import tkinter as tk
import threading
import click 

def iniciarPrograma():
    if not click.rodando:  
        click.iniciar()
        status.config(text="Rodando...")
        t = threading.Thread(target=click.localizarOferta, daemon=True)
        t.start()

def pararPrograma():
    click.parar()
    status.config(text="Parado")

# ---- INTERFACE ----
clickPoint = tk.Tk()
clickPoint.config(background='#1a1a40')
clickPoint.title('ClickPoint')
clickPoint.geometry('300x300')
clickPoint.resizable(False, False)

titulo = tk.Label(clickPoint, text='ClickPoint', fg='white', bg='#1a1a40', font=('Arial', 20))
titulo.pack(pady=10)

botao_iniciar = tk.Button(clickPoint, text='Iniciar', command=iniciarPrograma, width=15)
botao_iniciar.pack(pady=10)

botao_parar = tk.Button(clickPoint, text='Parar', command=pararPrograma, width=15)
botao_parar.pack(pady=10)

status = tk.Label(clickPoint, text='Aguardando...', fg='white', bg='#1a1a40')
status.pack(pady=10)

clickPoint.mainloop()


