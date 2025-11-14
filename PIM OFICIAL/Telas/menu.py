import customtkinter as ctk

from Telas.telacadastro import telacadastro
from Telas.telalogin import telalogin

def menu(tl):
    for widget in tl.winfo_children():
        widget.destroy()

# label

    label1 = ctk.CTkLabel (tl, text = 'Bem vindo(a) ao TechLearn!')
    label1.pack(pady=(90, 5))

    label2 = ctk.CTkLabel (tl, text = 'O ensino do futuro começa aqui')
    label2.pack(pady=(5, 0))

# botão

    botao1 = ctk.CTkButton(tl, text="Entrar", command=lambda: telalogin(tl))
    botao1.pack(pady=(25, 0))

    botao2 = ctk.CTkButton(tl, text="Cadastrar", command=lambda: telacadastro(tl))
    botao2.pack(pady=(25, 0))

    