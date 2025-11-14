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
        except:
            return []

def salvardados(dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def lancarnotas(tl):
    # Limpa a tela
    for widget in tl.winfo_children():
        widget.destroy()

    dados = carregardados()

    titulo = ctk.CTkLabel(tl, text="Lançar Notas", font=("Arial", 24))
    titulo.pack(pady=20)

    # === PEGAR TODAS AS TURMAS QUE EXISTEM NO ARQUIVO ===
    turmas_existentes = sorted(list({u["turma"] for u in dados if u.get("turma")}))

    combo_turmas = ctk.CTkComboBox(tl, values=turmas_existentes, width=200)
    combo_turmas.pack(pady=10)

    combo_alunos = ctk.CTkComboBox(tl, values=[], width=200)
    combo_alunos.pack(pady=10)

    # CAMPOS PARA NOTAS
    nota1 = ctk.CTkEntry(tl, placeholder_text="Nota 1", width=100)
    nota2 = ctk.CTkEntry(tl, placeholder_text="Nota 2", width=100)
    nota3 = ctk.CTkEntry(tl, placeholder_text="Nota 3", width=100)

    # Só aparecem após escolher aluno
    campos_notas = [nota1, nota2, nota3]

    msg = ctk.CTkLabel(tl, text="")
    msg.pack(pady=10)

    # -------------------------------
    # AO ESCOLHER UMA TURMA
    # -------------------------------
    def atualizaralunos(*args):
        turma = combo_turmas.get()

        alunos = [u["nome"] for u in dados
                  if u["tipo"] == "aluno" and u.get("turma") == turma]

        combo_alunos.configure(values=alunos)
        combo_alunos.set("")

        for campo in campos_notas:
            campo.pack_forget()
        msg.configure(text="")

    combo_turmas.configure(command=lambda _: atualizaralunos())

    # -------------------------------
    # AO ESCOLHER UM ALUNO
    # -------------------------------
    def mostrarcamposnotas(*args):
        if not combo_alunos.get():
            return

        # Exibe os campos de notas
        for campo in campos_notas:
            campo.pack(pady=5)

    combo_alunos.configure(command=lambda _: mostrarcamposnotas())

    # -------------------------------
    # SALVAR NOTAS
    # -------------------------------
    def salvarnotas():
        aluno_nome = combo_alunos.get()
        turma = combo_turmas.get()

        if not aluno_nome or not turma:
            msg.configure(text="Escolha turma e aluno!", text_color="red")
            return

        try:
            n1 = float(nota1.get())
            n2 = float(nota2.get())
            n3 = float(nota3.get())
        except:
            msg.configure(text="As notas precisam ser números!", text_color="red")
            return

        # Salva no JSON
        for u in dados:
            if u["nome"] == aluno_nome:
                u["notas"] = {
                    "nota1": n1,
                    "nota2": n2,
                    "nota3": n3
                }
                break

        salvardados(dados)

        msg.configure(text=f"Notas lançadas para {aluno_nome}!", text_color="green")

        nota1.delete(0, "end")
        nota2.delete(0, "end")
        nota3.delete(0, "end")

    botao_salvar = ctk.CTkButton(tl, text="Salvar Notas", command=salvarnotas)
    botao_salvar.pack(pady=20)

    # VOLTAR
    def voltar():
        from Telas.telaprofessor import telaprofessor
        telaprofessor(tl)

    ctk.CTkButton(tl, text="Voltar", command=voltar).pack(pady=10)
