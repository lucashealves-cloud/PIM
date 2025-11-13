import os
import json
import customtkinter as ctk

def telaprofessor(tl):
   # label

# ===================== BOTOES ===============================
   label1 = ctk.CTkLabel (tl, text = f"Olá Professor")
   label1.pack(pady=(90, 5))

   btnnotas = ctk.CTkButton (tl,text = "Notas")
   btnnotas.pack(pady=(20,0))

   btntrabalhos = ctk.CTkButton (tl,text = "Trabalhos")
   btntrabalhos.pack(pady=(20,0))

   btnturmas = ctk.CTkButton (tl,text = "Turmas")
   btnturmas.pack(pady=(20,0))