import json
import os
import customtkinter as ctk

from Telas import telaprofessor
from Telas import telaaluno

def telalogin(tl):
    
    for widget in tl.winfo_children():
        widget.destroy()
    
    # CAIXA DE TEXTOS
    titulocadastro = ctk.CTkLabel(tl, text="Login")
    titulocadastro.pack(pady=(90, 0))

    txt_email = ctk.CTkEntry(tl, placeholder_text="Digite seu email", width=250, height=35)
    txt_email.pack(pady=(20, 0))

    txt_senha = ctk.CTkEntry(tl, placeholder_text="Digite sua senha", show="*", width=250, height=35)
    txt_senha.pack(pady=(20, 0))

    msg_label = ctk.CTkLabel(tl, text="")
    msg_label.pack(pady=(10, 0))

    #====================================================================
    # AUTENTICAR LOGIN
    def loginautenticar(tl):
        email = txt_email.get().strip()
        senha = txt_senha.get().strip()

        if not email or not senha:
            msg_label.configure(text="Preencha os campos corretamente!", text_color="red")
            return
        
        arquivo = os.path.join(os.path.dirname(__file__), "usuarios.json")

        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                usuarios = json.load(f)
        except json.JSONDecodeError:
            msg_label.configure(text="Erro ao ler o arquivo de usuários!")
            return
        except FileNotFoundError:
            msg_label.configure(text="Arquivo de usuários não encontrado!")
            return

        # VERIFICAÇÃO
        for usuario in usuarios:
            if usuario["email"] == email and usuario["senha"] == senha:
                tipo = usuario["tipo"]
                
                # VERIFICAR SE É PROFESSOR

                matricula = usuario["matrícula"]

                if usuario["tipo"] == "professor":
                    for widget in tl.winfo_children():
                        widget.destroy()
                    telaprofessor.telaprofessor(tl)
                    return
                
                elif usuario["tipo"] == "aluno":
                    for widget in tl.winfo_children():
                        widget.destroy()
                    telaaluno.telaaluno(tl, matricula)
                    return
                
                # VERIFICAR SE É ALUNO
                for widget in tl.winfo_children():
                    widget.destroy()
                telaaluno.telaaluno(tl)
                return
        
        msg_label.configure(text="Email ou senha incorretos!")

    #==========================================================================
    # BOTOES  
    entrarbtn = ctk.CTkButton(tl, text="Entrar", command=lambda: loginautenticar(tl))
    entrarbtn.pack(pady=(20, 0))

    voltarbtn = ctk.CTkButton(tl, text="Voltar", command=lambda: voltar(tl))
    voltarbtn.pack(side="left", pady=0)

    def voltar(tl):
        from Telas.menu import menu
        for widget in tl.winfo_children():
            widget.destroy()
        menu(tl)