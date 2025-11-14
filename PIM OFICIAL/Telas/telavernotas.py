import customtkinter as ctk
import json

def telavernotas(tl, matricula):

    for widget in tl.winfo_children():
        widget.destroy()

    # ABRE O ARQUIVO CERTO
    with open("usuarios.json", "r", encoding="utf-8") as arq:
        alunos = json.load(arq)

    # PROCURAR ALUNO PELA MATRÍCULA
    aluno = None
    for a in alunos:
        if a.get("matrícula") == matricula:
            aluno = a
            break

    # SE NÃO ACHOU
    if aluno is None:
        ctk.CTkLabel(tl, text="Aluno não encontrado").pack(pady=20)
        return

    # NOTAS
    n1 = aluno["notas"]["nota1"]
    n2 = aluno["notas"]["nota2"]
    n3 = aluno["notas"]["nota3"]




    # INTERFACE
    ctk.CTkLabel(tl, text="Suas Notas", font=("Arial", 20)).pack(pady=10)
    ctk.CTkLabel(tl, text=f"Nota 1: {n1}").pack(pady=5)
    ctk.CTkLabel(tl, text=f"Nota 2: {n2}").pack(pady=5)
    ctk.CTkLabel(tl, text=f"Nota 3: {n3}").pack(pady=5)

    ctk.CTkButton(tl, text="Voltar", command=lambda: print("voltar aqui")).pack(pady=15)