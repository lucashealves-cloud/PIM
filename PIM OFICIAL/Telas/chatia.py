import customtkinter as ctk
import openai
from Telas import telaaluno

openai.api_key = ""

def chatia(tl):

    for widget in tl.winfo_children():
        widget.destroy()

    tl.title("Assistente Wallace - Aluno")

    def enviar_mensagem():
        texto = entrada.get()
        if texto.strip() == "":
            return
        
        chatbox.configure(state="normal")
        chatbox.insert("end", f"Você: {texto}\n")
        chatbox.configure(state="disabled")
        chatbox.yview_moveto(1)

        entrada.delete(0, "end")

        try:
            resposta = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Você é um chatbot simpático ajudando alunos."},
                    {"role": "user", "content": texto}
                ]
            )
            bot = resposta.choices[0].message["content"]

            chatbox.configure(state="normal")
            chatbox.insert("end", f"Bot: {bot}\n\n")
            chatbox.configure(state="disabled")
            chatbox.yview_moveto(1)

        except Exception as e:
            chatbox.configure(state="normal")
            chatbox.insert("end", f"ERRO ao conectar com a API: {e}\n\n")
            chatbox.configure(state="disabled")

    titulo = ctk.CTkLabel(tl, text="Assistente Wallace", font=("Arial", 22))
    titulo.pack(pady=20)

    chatbox = ctk.CTkTextbox(tl, width=500, height=350, state="disabled", font=("Arial", 15))
    chatbox.pack(pady=10)

    entrada = ctk.CTkEntry(tl, width=400, placeholder_text="Digite sua mensagem...")
    entrada.pack(side="left", padx=(40, 10), pady=10)

    enviar_btn = ctk.CTkButton(tl, text="Enviar", width=100, command=enviar_mensagem)
    enviar_btn.pack(side="left", pady=10)

    from Telas.menu import menu
    voltar = ctk.CTkButton(tl, text="Voltar", width=100, fg_color="gray", command=lambda: telaaluno.telaaluno(tl))
    voltar.pack(pady=20)
