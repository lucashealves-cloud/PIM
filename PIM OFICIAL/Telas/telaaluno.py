import os
import json
import customtkinter as ctk
from Telas import telalogin, telacadastro

def telaaluno(tl):
   # label

   label1 = ctk.CTkLabel (tl, text = f"Olá aluno")
   label1.pack(pady=(90, 5))

   btnnotas = ctk.CTkButton (tl,text = "Notas")
   btnnotas.pack(pady=(20,0))

   btntrabalhos = ctk.CTkButton (tl,text = "Trabalhos")
   btntrabalhos.pack(pady=(20,0))

   btntrabalhos = ctk.CTkButton (tl,text = "Perfil")
   btntrabalhos.pack(pady=(20,0))