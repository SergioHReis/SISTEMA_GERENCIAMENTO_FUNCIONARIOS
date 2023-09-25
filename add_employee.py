import tkinter as tk
from tkinter import ttk, messagebox
import re
import csv

class AplicacaoGerenciamentoFuncionarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciar Funcionários")
        self.funcionarios = []

        self.criar_interface()
        self.criar_tabela()

    def criar_interface(self):
        self.frame_pessoal = ttk.LabelFrame(root, text="Informações Pessoais")
        self.frame_pessoal.pack(padx=10, pady=10, fill='both', expand='yes')

        self.label_nome = tk.Label(self.frame_pessoal, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entrada_nome = tk.Entry(self.frame_pessoal)
        self.entrada_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_data_nascimento = tk.Label(self.frame_pessoal, text="Data de Nascimento (DD/MM/AAAA):")
        self.label_data_nascimento.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entrada_data_nascimento = tk.Entry(self.frame_pessoal)
        self.entrada_data_nascimento.grid(row=1, column=1, padx=5, pady=5)

        self.label_email = tk.Label(self.frame_pessoal, text="Endereço de E-mail:")
        self.label_email.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.entrada_email = tk.Entry(self.frame_pessoal)
        self.entrada_email.grid(row=2, column=1, padx=5, pady=5)

        self.frame_profissional = ttk.LabelFrame(root, text="Informações Profissionais")
        self.frame_profissional.pack(padx=10, pady=10, fill='both', expand='yes')

        self.label_cargo = tk.Label(self.frame_profissional, text="Cargo:")
        self.label_cargo.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entrada_cargo = tk.Entry(self.frame_profissional)
        self.entrada_cargo.grid(row=0, column=1, padx=5, pady=5)

        self.label_departamento = tk.Label(self.frame_profissional, text="Departamento:")
        self.label_departamento.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entrada_departamento = tk.Entry(self.frame_profissional)
        self.entrada_departamento.grid(row=1, column=1, padx=5, pady=5)

        self.label_salario_hora = tk.Label(self.frame_profissional, text="Salário por Hora (R$):")
        self.label_salario_hora.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.entrada_salario_hora = tk.Entry(self.frame_profissional)
        self.entrada_salario_hora.grid(row=2, column=1, padx=5, pady=5)

        self.frame_endereco_alugueis = ttk.LabelFrame(root, text="Endereço e Aluguéis")
        self.frame_endereco_alugueis.pack(padx=10, pady=10, fill='both', expand='yes')

        self.label_endereco = tk.Label(self.frame_endereco_alugueis, text="Endereço Atual:")
        self.label_endereco.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entrada_endereco = tk.Entry(self.frame_endereco_alugueis)
        self.entrada_endereco.grid(row=0, column=1, padx=5, pady=5)

        self.label_aluguel_carro = tk.Label(self.frame_endereco_alugueis, text="Aluguel de Carro:")
        self.label_aluguel_carro.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.var_aluguel_carro = tk.StringVar()
        self.var_aluguel_carro.set("Não")
        self.radio_sim_carro = tk.Radiobutton(self.frame_endereco_alugueis, text="Sim", variable=self.var_aluguel_carro, value="Sim")
        self.radio_sim_carro.grid(row=1, column=1, padx=5, pady=5)
        self.radio_nao_carro = tk.Radiobutton(self.frame_endereco_alugueis, text="Não", variable=self.var_aluguel_carro, value="Não")
        self.radio_nao_carro.grid(row=1, column=2, padx=5, pady=5)

        self.label_valor_aluguel_carro = tk.Label(self.frame_endereco_alugueis, text="Valor do Aluguel de Carro (R$):")
        self.label_valor_aluguel_carro.grid(row=1, column=3, padx=5, pady=5, sticky='w')
        self.entrada_valor_aluguel_carro = tk.Entry(self.frame_endereco_alugueis)
        self.entrada_valor_aluguel_carro.grid(row=1, column=4, padx=5, pady=5)

        self.label_aluguel_notebook = tk.Label(self.frame_endereco_alugueis, text="Aluguel de Notebook:")
        self.label_aluguel_notebook.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.var_aluguel_notebook = tk.StringVar()
        self.var_aluguel_notebook.set("Não")
        self.radio_sim_notebook = tk.Radiobutton(self.frame_endereco_alugueis, text="Sim", variable=self.var_aluguel_notebook, value="Sim")
        self.radio_sim_notebook.grid(row=2, column=1, padx=5, pady=5)
        self.radio_nao_notebook = tk.Radiobutton(self.frame_endereco_alugueis, text="Não", variable=self.var_aluguel_notebook, value="Não")
        self.radio_nao_notebook.grid(row=2, column=2, padx=5, pady=5)

        self.label_valor_aluguel_notebook = tk.Label(self.frame_endereco_alugueis, text="Valor do Aluguel de Notebook (R$):")
        self.label_valor_aluguel_notebook.grid(row=2, column=3, padx=5, pady=5, sticky='w')
        self.entrada_valor_aluguel_notebook = tk.Entry(self.frame_endereco_alugueis)
        self.entrada_valor_aluguel_notebook.grid(row=2, column=4, padx=5, pady=5)

        self.label_aluguel_celular = tk.Label(self.frame_endereco_alugueis, text="Aluguel de Celular:")
        self.label_aluguel_celular.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.var_aluguel_celular = tk.StringVar()
        self.var_aluguel_celular.set("Não")
        self.radio_sim_celular = tk.Radiobutton(self.frame_endereco_alugueis, text="Sim", variable=self.var_aluguel_celular, value="Sim")
        self.radio_sim_celular.grid(row=3, column=1, padx=5, pady=5)
        self.radio_nao_celular = tk.Radiobutton(self.frame_endereco_alugueis, text="Não", variable=self.var_aluguel_celular, value="Não")
        self.radio_nao_celular.grid(row=3, column=2, padx=5, pady=5)

        self.label_valor_aluguel_celular = tk.Label(self.frame_endereco_alugueis, text="Valor do Aluguel de Celular (R$):")
        self.label_valor_aluguel_celular.grid(row=3, column=3, padx=5, pady=5, sticky='w')
        self.entrada_valor_aluguel_celular = tk.Entry(self.frame_endereco_alugueis)
        self.entrada_valor_aluguel_celular.grid(row=3, column=4, padx=5, pady=5)

        self.botao_adicionar = tk.Button(root, text="Adicionar Funcionário", command=self.adicionar_funcionario)
        self.botao_adicionar.pack(pady=10)

        self.botao_excluir = tk.Button(root, text="Excluir Funcionário", command=self.excluir_funcionario)
        self.botao_excluir.pack(pady=10)

        self.botao_relatorio_csv = tk.Button(root, text="Baixar Relatório CSV", command=self.baixar_relatorio_csv)
        self.botao_relatorio_csv.pack(pady=10)

    def criar_tabela(self):
        self.lista_funcionarios = ttk.Treeview(root, columns=("Nome", "Data de Nascimento", "E-mail", "Cargo", "Departamento", "Salário por Hora", "Endereço", "Aluguel de Carro", "Valor do Aluguel de Carro", "Aluguel de Notebook", "Valor do Aluguel de Notebook", "Aluguel de Celular", "Valor do Aluguel de Celular"))
        self.lista_funcionarios.heading("#1", text="Nome")
        self.lista_funcionarios.heading("#2", text="Data de Nascimento")
        self.lista_funcionarios.heading("#3", text="E-mail")
        self.lista_funcionarios.heading("#4", text="Cargo")
        self.lista_funcionarios.heading("#5", text="Departamento")
        self.lista_funcionarios.heading("#6", text="Salário por Hora")
        self.lista_funcionarios.heading("#7", text="Endereço")
        self.lista_funcionarios.heading("#8", text="Aluguel de Carro")
        self.lista_funcionarios.heading("#9", text="Valor do Aluguel de Carro")
        self.lista_funcionarios.heading("#10", text="Aluguel de Notebook")
        self.lista_funcionarios.heading("#11", text="Valor do Aluguel de Notebook")
        self.lista_funcionarios.heading("#12", text="Aluguel de Celular")
        self.lista_funcionarios.heading("#13", text="Valor do Aluguel de Celular")
        self.lista_funcionarios.pack()

    def adicionar_funcionario(self):
        nome = self.entrada_nome.get()
        data_nascimento = self.entrada_data_nascimento.get()
        email = self.entrada_email.get()
        cargo = self.entrada_cargo.get()
        departamento = self.entrada_departamento.get()
        salario_hora = self.entrada_salario_hora.get()
        endereco = self.entrada_endereco.get()
        aluguel_carro = self.var_aluguel_carro.get()
        valor_aluguel_carro = self.entrada_valor_aluguel_carro.get()
        aluguel_notebook = self.var_aluguel_notebook.get()
        valor_aluguel_notebook = self.entrada_valor_aluguel_notebook.get()
        aluguel_celular = self.var_aluguel_celular.get()
        valor_aluguel_celular = self.entrada_valor_aluguel_celular.get()

        if not nome or not data_nascimento or not email or not cargo or not departamento or not salario_hora or not endereco:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
            return

        try:
            salario_hora = float(salario_hora)
            valor_aluguel_carro = float(valor_aluguel_carro)
            valor_aluguel_notebook = float(valor_aluguel_notebook)
            valor_aluguel_celular = float(valor_aluguel_celular)
        except ValueError:
            messagebox.showerror("Erro", "Os campos numéricos devem conter valores válidos.")
            return

        if not re.match(r'\d{2}/\d{2}/\d{4}', data_nascimento):
            messagebox.showerror("Erro", "Formato de data inválido. Use DD/MM/AAAA.")
            return

        self.funcionarios.append({
            "Nome": nome,
            "Data de Nascimento": data_nascimento,
            "E-mail": email,
            "Cargo": cargo,
            "Departamento": departamento,
            "Salário por Hora": salario_hora,
            "Endereço": endereco,
            "Aluguel de Carro": aluguel_carro,
            "Valor do Aluguel de Carro": valor_aluguel_carro,
            "Aluguel de Notebook": aluguel_notebook,
            "Valor do Aluguel de Notebook": valor_aluguel_notebook,
            "Aluguel de Celular": aluguel_celular,
            "Valor do Aluguel de Celular": valor_aluguel_celular
        })

        self.atualizar_tabela()

        messagebox.showinfo("Funcionário Adicionado", "Funcionário adicionado com sucesso!")

    def excluir_funcionario(self):
        item_selecionado = self.lista_funcionarios.selection()
        if not item_selecionado:
            messagebox.showerror("Erro", "Selecione um funcionário para excluir.")
            return

        confirmacao = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir o funcionário selecionado?")
        if confirmacao:
            for item in item_selecionado:
                index = int(item.split("_")[1]) - 1
                del self.funcionarios[index]
            self.atualizar_tabela()
            messagebox.showinfo("Funcionário Excluído", "Funcionário excluído com sucesso!")

    def baixar_relatorio_csv(self):
        if not self.funcionarios:
            messagebox.showerror("Erro", "A lista de funcionários está vazia.")
            return

        with open("relatorio_funcionarios.csv", "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["Nome", "Data de Nascimento", "E-mail", "Cargo", "Departamento", "Salário por Hora", "Endereço", "Aluguel de Carro", "Valor do Aluguel de Carro", "Aluguel de Notebook", "Valor do Aluguel de Notebook", "Aluguel de Celular", "Valor do Aluguel de Celular"])
            for funcionario in self.funcionarios:
                csvwriter.writerow([
                    funcionario["Nome"],
                    funcionario["Data de Nascimento"],
                    funcionario["E-mail"],
                    funcionario["Cargo"],
                    funcionario["Departamento"],
                    funcionario["Salário por Hora"],
                    funcionario["Endereço"],
                    funcionario["Aluguel de Carro"],
                    funcionario["Valor do Aluguel de Carro"],
                    funcionario["Aluguel de Notebook"],
                    funcionario["Valor do Aluguel de Notebook"],
                    funcionario["Aluguel de Celular"],
                    funcionario["Valor do Aluguel de Celular"]
                ])

        messagebox.showinfo("Relatório Gerado", "Relatório de funcionários gerado com sucesso como relatorio_funcionarios.csv.")

    def atualizar_tabela(self):
        for i in self.lista_funcionarios.get_children():
            self.lista_funcionarios.delete(i)

        for index, funcionario in enumerate(self.funcionarios, start=1):
            self.lista_funcionarios.insert("", "end", values=(
                funcionario["Nome"],
                funcionario["Data de Nascimento"],
                funcionario["E-mail"],
                funcionario["Cargo"],
                funcionario["Departamento"],
                funcionario["Salário por Hora"],
                funcionario["Endereço"],
                funcionario["Aluguel de Carro"],
                funcionario["Valor do Aluguel de Carro"],
                funcionario["Aluguel de Notebook"],
                funcionario["Valor do Aluguel de Notebook"],
                funcionario["Aluguel de Celular"],
                funcionario["Valor do Aluguel de Celular"]
            ))


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoGerenciamentoFuncionarios(root)
    root.mainloop()
