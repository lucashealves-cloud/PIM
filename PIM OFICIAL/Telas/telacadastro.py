import json
import os
import random
import customtkinter as ctk

def telacadastro(tl):
    from Telas.menu import menu
    
    for widget in tl.winfo_children():
        widget.destroy()
    
    # CAIXA DE TEXTOS
    titulocadastro = ctk.CTkLabel(tl, text="Cadastro")
    titulocadastro.pack(pady=(90, 0))

    txt_nome = ctk.CTkEntry(tl, placeholder_text="Digite seu nome", width=250, height=35)
    txt_nome.pack(pady=(20, 0))

    txt_email = ctk.CTkEntry(tl, placeholder_text="Digite seu email", width=250, height=35)
    txt_email.pack(pady=(20, 0))

    txt_senha = ctk.CTkEntry(tl, placeholder_text="Digite sua senha", show="*", width=250, height=35)
    txt_senha.pack(pady=(20, 0))

    msg_label = ctk.CTkLabel(tl, text="")
    msg_label.pack(pady=(10, 0))


    # GERANDO MATRÍCULA ===================================
    def gerar_matricula():
        return f"{random.randint(1000, 9999)}TL"


    #==========================================================================================================
    # FUNÇÃO SALVA OS DADOS
    #==========================================================================================================

    def cadastrocriado():
        email = txt_email.get().strip()
        nome = txt_nome.get().strip()
        senha = txt_senha.get().strip()

        if not nome or not email or not senha:
            msg_label.configure(text="⚠️ Preencha todos os campos corretamente!", text_color="red")
            return

        if "@techlearn.com" in email:
            tipo = "professor"
            matricula = None
        else:
            tipo = "aluno"
            matricula = gerar_matricula()
            
        usuario = {
            "nome": nome,
            "email": email,
            "tipo": tipo,
            "senha": senha,
            "matrícula": matricula
        }

        arquivo = os.path.join(os.path.dirname(__file__), "usuarios.json")

        # LÊ OS DADOS EXISTENTES
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = []
        else:
            dados = []

        # ADICIONA O NOVO USUÁRIO
        dados.append(usuario)

        # SALVA NO ARQUIVO
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        msg_label.configure(text="✅ Cadastro criado com sucesso!", text_color="green")

        # LIMPA OS CAMPOS
        txt_nome.delete(0, "end")
        txt_email.delete(0, "end")
        txt_senha.delete(0, "end")

    #================================================================================================
    # BOTÕES
    #================================================================================================

    entrarbtn = ctk.CTkButton(tl, text="Cadastrar", command=cadastrocriado)
    entrarbtn.pack(pady=(20, 0))

    voltarbtn = ctk.CTkButton(tl, text="Voltar", command=lambda: voltarparamenu(tl))
    voltarbtn.pack(side="left", pady=0)

    def voltarparamenu(tl):
        from Telas.menu import menu
        for widget in tl.winfo_children():
            widget.destroy()
        menu(tl)
