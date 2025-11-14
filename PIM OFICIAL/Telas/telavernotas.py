import os
import customtkinter as ctk
import json
import subprocess

from Telas import telaaluno

def calcular_media_c(n1, n2, n3):

    arquivo = os.path.join(os.path.dirname(__file__), "notas.exe")

    processo = subprocess.Popen(
        [arquivo, str(n1), str(n2), str(n3)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    saida, erro = processo.communicate()

    if erro:
        print("Erro no C:", erro)

    try:
        return float(saida.strip())
    except:
        return None

def telavernotas(tl, matricula):

    for widget in tl.winfo_children():
        widget.destroy()

    # CAMINHO CORRETO DO JSON
    arquivo = os.path.join(os.path.dirname(__file__), "usuarios.json")

    # ABRE O ARQUIVO JSON USANDO O CAMINHO CORRETO
    with open(arquivo, "r", encoding="utf-8") as arq:
        alunos = json.load(arq)

    # PROCURAR ALUNO PELA MATRÍCULA
    aluno = next((a for a in alunos if a.get("matrícula") == matricula), None)

    if aluno is None:
        ctk.CTkLabel(tl, text="Aluno não encontrado").pack(pady=20)
        return

    # PEGAR NOTAS
    n1 = aluno["notas"]["nota1"]
    n2 = aluno["notas"]["nota2"]
    n3 = aluno["notas"]["nota3"]

    # CALCULAR MÉDIA USANDO O C
    media = calcular_media_c(n1, n2, n3)

    # INTERFACE
    ctk.CTkLabel(tl, text="Suas Notas").pack(pady=40)
    ctk.CTkLabel(tl, text=f"NP1: {n1}").pack(pady=15)
    ctk.CTkLabel(tl, text=f"NP2: {n2}").pack(pady=15)
    ctk.CTkLabel(tl, text=f"NP3: {n3}").pack(pady=15)

    # MOSTRA A MÉDIA DO C
    if media is not None:
        ctk.CTkLabel(tl, text=f"Média: {media:.2f}").pack(pady=10)
    else:
        ctk.CTkLabel(tl, text="Erro ao calcular média no C").pack(pady=10)

    ctk.CTkButton(tl, text="Voltar", command=lambda: telaaluno.telaaluno())
