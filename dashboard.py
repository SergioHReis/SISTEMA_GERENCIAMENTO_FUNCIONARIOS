import tkinter as tk

class AplicacaoDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Painel de Controle")

        self.label = tk.Label(root, text="Bem-vindo ao Sistema de Gerenciamento de Funcionários")
        self.label.pack()

        # Adicione componentes GUI para exibir informações e funcionalidades aqui

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoDashboard(root)
    root.mainloop()
