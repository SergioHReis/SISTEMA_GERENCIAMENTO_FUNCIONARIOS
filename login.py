import tkinter as tk
from tkinter import messagebox

class AplicacaoLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        self.label_usuario = tk.Label(root, text="Usuário:")
        self.label_usuario.pack()
        self.entrada_usuario = tk.Entry(root)
        self.entrada_usuario.pack()

        self.label_senha = tk.Label(root, text="Senha:")
        self.label_senha.pack()
        self.entrada_senha = tk.Entry(root, show="*")
        self.entrada_senha.pack()

        self.botao_login = tk.Button(root, text="Login", command=self.efetuar_login)
        self.botao_login.pack()

    def efetuar_login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()

        # Verifique as credenciais do usuário aqui (compare com um banco de dados de usuários)

        if usuario == "admin" and senha == "admin123":
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.root.destroy()
            # Chame o módulo principal do sistema aqui (dashboard.py, por exemplo)
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha inválidos")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoLogin(root)
    root.mainloop()
