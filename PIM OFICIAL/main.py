import os
import customtkinter as ctk
from Telas.menu import menu
from Telas.telacadastro import telacadastro
from Telas.telalogin import telalogin

#aparencia
ctk.set_appearance_mode("dark")

#janela
tl = ctk.CTk()
tl.title("Login")
tl.geometry("800x600")

#tellas

menu(tl)

tl.mainloop()