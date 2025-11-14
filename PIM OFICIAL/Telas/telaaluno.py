
import customtkinter as ctk

from Telas import menu, telavernotas
from Telas import chatia
def telaaluno(tl, matricula):

    # Limpa a tela antes de montar a interface
    for widget in tl.winfo_children():
        widget.destroy()

    # Título
    titulo = ctk.CTkLabel(tl, text="Área do Aluno", font=("Arial", 24))
    titulo.pack(pady=(50, 10))

    # Subtítulo
    subtitulo = ctk.CTkLabel(tl, text="Bem-vindo(a) ao seu painel!")
    subtitulo.pack(pady=(0, 20))

    # Botão – Notas
    btn_notas = ctk.CTkButton(tl,text="Ver Notas",width=200,command=lambda: telavernotas.telavernotas(tl, matricula))
    btn_notas.pack(pady=10)

    # Botão - Assistente Virtual IA
    btn_trabalhos = ctk.CTkButton(tl,text="Assistente Virtual", width=200, command=lambda: chatia.chatia(tl))
    btn_trabalhos.pack(pady=10)

    # Botão – Sair
    btn_sair = ctk.CTkButton(
        tl,
        text="Sair",
        fg_color="red",
        hover_color="#8b0000",
        width=200,
        command=lambda: menu.menu(tl)
    )
    btn_sair.pack(pady=30)