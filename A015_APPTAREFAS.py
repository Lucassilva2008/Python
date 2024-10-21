# Aplicativo desktop Tarefas
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

tarefas = []
def adicionar_tarefa():
    tarefa = entry_tarefa.get()
    if tarefa:
        tarefas.append({"tarefa" : tarefa, "data": datetime.now()})
        listbox_tarefas.insert(tk.END, f"{tarefa}- {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        #messagebox.showinfo("Minhas Tarefas", tarefas)

        entry_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso!", "Digite uma Tarefa!")

def concluir_tarefa():
    indice_selecionado = listbox_tarefas.curselection()
    if indice_selecionado:
        tarefa_concluida = tarefas.pop(indice_selecionado[0])
        listbox_tarefas.delete(indice_selecionado)
        messagebox.showinfo("Concluido", f"Tarefa \'{tarefa_concluida['tarefa']}\' Concluida")


def função():
    entrada = entry_tarefa.get()
    if entrada:
        messagebox.showinfo("Tarefa", entrada)
    else:
        messagebox.showerror("Hei!", "Faltou a mensagem! ")

root = tk.Tk()
root.title("Gerenciador de Tarefa")

label = tk.Label(root, text="Tarefas da Escola Estadual \nDr. Ângelo Mendes de Almeida", width=50)
label.pack(pady=8)

entry_tarefa = tk.Entry(root, width=40)
entry_tarefa.pack(pady=5)

botao_adicionar = tk.Button(root, width=30, text="Adicionar Tarefa", command= adicionar_tarefa)
botao_adicionar.pack(pady=10)

listbox_tarefas = tk.Listbox(root, width=40, height=10)
listbox_tarefas.pack()

botao_concluir = tk.Button(root, text="Concluir Tarefa", command=concluir_tarefa)
botao_concluir.pack(pady=10)
root.mainloop()