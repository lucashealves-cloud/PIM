import json
import os
import customtkinter as ctk

# Caminho do JSON
arquivo = os.path.join(os.path.dirname(__file__), "usuarios.json")

def carregardados():
    if not os.path.exists(arquivo):
        return []

    with open(arquivo, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def salvardados(dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def gerenciarturmas(tl):
    # Limpa tela
    for widget in tl.winfo_children():
        widget.destroy()

    titulo = ctk.CTkLabel(tl, text="Gerenciar Turmas", font=("Arial", 24))
    titulo.pack(pady=20)

    # Carregar usuários
    dados = carregardados()

    # Listas
    turmas = ["Turma A", "Turma B", "Turma C"]
    alunos_sem_turma = [u for u in dados if u["tipo"] == "aluno" and not u.get("turma")]
    alunos_com_turma = [u for u in dados if u["tipo"] == "aluno" and u.get("turma")]

    # Combobox turmas
    combo_turmas = ctk.CTkComboBox(tl, values=turmas, width=200)
    combo_turmas.pack(pady=10)

    # Combobox alunos
    combo_alunos = ctk.CTkComboBox(
        tl,
        values=[a["nome"] for a in alunos_sem_turma],
        width=200
    )
    combo_alunos.pack(pady=10)

    msg = ctk.CTkLabel(tl, text="")
    msg.pack(pady=10)

    # Botão para adicionar aluno na turma
    def adicionaraluno():
        nome_aluno = combo_alunos.get()
        turma_escolhida = combo_turmas.get()

        if not nome_aluno or not turma_escolhida:
            msg.configure(text="Escolha o aluno e a turma!", text_color="red")
            return

        # Atualiza no JSON
        for u in dados:
            if u["nome"] == nome_aluno:
                u["turma"] = turma_escolhida
                break

        salvardados(dados)

        msg.configure(text=f"{nome_aluno} agora está em {turma_escolhida}", text_color="green")

        # Atualiza combobox
        combo_alunos.configure(
            values=[a["nome"] for a in carregardados() if a["tipo"]=="aluno" and not a.get("turma")]
        )
        combo_alunos.set("")

    btn_add = ctk.CTkButton(tl, text="Adicionar Aluno à Turma", command=adicionaraluno)
    btn_add.pack(pady=15)

    # Botão voltar
    def voltar():
        from Telas.telaprofessor import telaprofessor
        telaprofessor(tl)

    btn_voltar = ctk.CTkButton(tl, text="Voltar", command=voltar)
    btn_voltar.pack(pady=10)