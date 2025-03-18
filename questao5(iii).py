import tkinter as tk
from tkinter import messagebox

class MiniAkinator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini-Akinator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.perguntas = [
            ("O personagem é real?", "real"),
            ("O personagem é um homem?", "homem"),
            ("O personagem é um super-herói?", "superheroi"),
            ("O personagem é um cientista?", "cientista"),
            ("O personagem tem poderes mágicos?", "magico"),
            ("O personagem é um vilão?", "vilao"),
            ("O personagem é um jogador de futebol?", "futebol"),
            ("O personagem é um cantor famoso?", "cantor"),
            ("O personagem faz parte de um desenho animado?", "desenho"),
            ("O personagem é de um anime?", "anime"),
            ("O personagem é um protagonista?", "protagonista"),
            ("O personagem usa uma espada?", "espada"),
            ("O personagem faz parte de um jogo?", "jogo")
        ]
        
        self.regras = {
            ("real", "homem", "cientista"): "Albert Einstein",
            ("real", "homem", "superheroi"): "Homem de Ferro",
            ("real", "homem"): "Leonardo da Vinci",
            ("real",): "Cleópatra",
            ("superheroi",): "Superman",
            ("magico",): "Harry Potter",
            ("vilao", "superheroi"): "Coringa",
            ("vilao", "magico"): "Voldemort",
            ("real", "homem", "futebol"): "Pelé",
            ("real", "homem", "cantor"): "Michael Jackson",
            ("real", "homem", "desenho"): "Walt Disney",
            ("desenho", "superheroi"): "Batman",
            ("desenho", "magico"): "Mickey Mouse",
            ("desenho", "vilao"): "Scar (Rei Leão)",
            ("anime", "protagonista", "espada"): "Guts (Berserk)",
            ("anime", "protagonista", "magico"): "Naruto Uzumaki",
            ("anime", "vilao"): "Freeza (Dragon Ball)",
            ("jogo", "protagonista", "espada"): "Link (The Legend of Zelda)",
            ("jogo", "protagonista"): "Mario (Super Mario Bros)"
        }
        
        self.respostas = []
        self.pergunta_atual = 0
        
        self.label_pergunta = tk.Label(self.root, text="", font=("Arial", 14), wraplength=350)
        self.label_pergunta.pack(pady=20)
        
        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack()
        
        self.btn_sim = tk.Button(self.frame_buttons, text="Sim", command=lambda: self.responder("sim"), width=10)
        self.btn_sim.grid(row=0, column=0, padx=10)
        
        self.btn_nao = tk.Button(self.frame_buttons, text="Não", command=lambda: self.responder("nao"), width=10)
        self.btn_nao.grid(row=0, column=1, padx=10)
        
        self.fazer_pergunta()
        self.root.mainloop()
        
    def fazer_pergunta(self):
        if self.pergunta_atual < len(self.perguntas):
            self.label_pergunta.config(text=self.perguntas[self.pergunta_atual][0])
        else:
            self.inferir_personagem()
        
    def responder(self, resposta):
        if resposta == "sim":
            self.respostas.append(self.perguntas[self.pergunta_atual][1])
        self.pergunta_atual += 1
        self.fazer_pergunta()
        
    def inferir_personagem(self):
        for regra, personagem in self.regras.items():
            if all(r in self.respostas for r in regra):
                messagebox.showinfo("Resultado", f"Seu personagem é: {personagem}")
                self.root.quit()
                return
        messagebox.showinfo("Resultado", "Não consegui adivinhar o personagem.")
        self.root.quit()

if __name__ == "__main__":
    MiniAkinator()
