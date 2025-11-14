import customtkinter as ctk

from Telas import gerenciarturmas, lancarnotas, menu

def telaprofessor(tl):

    # Limpa a tela
    for widget in tl.winfo_children():
        widget.destroy()

    # Título
    titulo = ctk.CTkLabel(tl, text="Área do Professor", font=("Arial", 24))
    titulo.pack(pady=(50, 10))

    # Subtítulo
    subtitulo = ctk.CTkLabel(tl, text="Gerencie suas turmas e alunos")
    subtitulo.pack(pady=(0, 20))

    # Botão – Lançar Notas
    btn_lancar_notas = ctk.CTkButton(tl,text="Lançar Notas",width=220,command=lambda: lancarnotas.lancarnotas(tl))
    btn_lancar_notas.pack(pady=10)

    # Botão – Ver Trabalhos Enviados
    btn_ver_trabalhos = ctk.CTkButton(
        tl,
        text="Ver Trabalhos dos Alunos",
        width=220,
        command=lambda: print("Abrindo trabalhos...")
    )
    btn_ver_trabalhos.pack(pady=10)

    # Botão – Gerenciar Turmas
    btn_turmas = ctk.CTkButton(tl, text="Gerenciar Turmas", width=220,command=lambda: gerenciarturmas.gerenciarturmas(tl))
    btn_turmas.pack(pady=10)

    # Botão – Perfil
    btn_perfil = ctk.CTkButton(tl, text="Perfil",width=220,command=lambda: print("Abrir perfil do professor..."))
    btn_perfil.pack(pady=10)

    # Botão – Sair
    btn_sair = ctk.CTkButton(tl, text="Sair", fg_color="red", hover_color="#8b0000", width=220, command=lambda: menu.menu(tl))
    btn_sair.pack(pady=30)