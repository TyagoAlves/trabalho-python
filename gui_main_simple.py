import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class SistemaEscolarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Escolar")
        self.root.geometry("700x500")
        
        # Conectar ao banco
        self.conn = sqlite3.connect('Banco.db')
        self.cursor = self.conn.cursor()
        self.criar_tabelas()
        
        self.criar_interface()
    
    def criar_tabelas(self):
        """Cria as tabelas do banco de dados"""
        sqls = [
            """CREATE TABLE IF NOT EXISTS ALUNOS(
                ID INTEGER NOT NULL,
                NOME TEXT NOT NULL,
                PRIMARY KEY (ID AUTOINCREMENT)
            );""",
            """CREATE TABLE IF NOT EXISTS DISCIPLINAS(
                ID INTEGER NOT NULL,
                NOME TEXT NOT NULL,
                PRIMARY KEY (ID AUTOINCREMENT)
            );""",
            """CREATE TABLE IF NOT EXISTS NOTAS(
                ID INTEGER NOT NULL,
                ID_ALUNO INTEGER NOT NULL,
                ID_DISCIPLINA INTEGER NOT NULL,
                NOTA REAL NOT NULL,
                PRIMARY KEY (ID AUTOINCREMENT),
                FOREIGN KEY (ID_ALUNO) REFERENCES ALUNOS(ID),
                FOREIGN KEY (ID_DISCIPLINA) REFERENCES DISCIPLINAS(ID)
            );"""
        ]
        
        for sql in sqls:
            self.cursor.execute(sql)
        self.conn.commit()
    
    def criar_interface(self):
        """Cria a interface gráfica"""
        # Título
        titulo = tk.Label(self.root, text="Sistema Escolar", 
                         font=("Arial", 20, "bold"))
        titulo.pack(pady=20)
        
        # Frame principal
        frame_main = ttk.Frame(self.root)
        frame_main.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Notebook (abas)
        notebook = ttk.Notebook(frame_main)
        notebook.pack(expand=True, fill='both')
        
        # Aba Alunos
        self.criar_aba_alunos(notebook)
        
        # Aba Disciplinas
        self.criar_aba_disciplinas(notebook)
        
        # Aba Notas
        self.criar_aba_notas(notebook)
    
    def criar_aba_alunos(self, notebook):
        """Cria aba para gerenciar alunos"""
        frame_alunos = ttk.Frame(notebook)
        notebook.add(frame_alunos, text="Alunos")
        
        # Inserir aluno
        ttk.Label(frame_alunos, text="Nome do Aluno:").pack(pady=5)
        self.entry_aluno = ttk.Entry(frame_alunos, width=30)
        self.entry_aluno.pack(pady=5)
        
        ttk.Button(frame_alunos, text="Inserir Aluno", 
                  command=self.inserir_aluno).pack(pady=5)
        
        # Lista de alunos
        ttk.Label(frame_alunos, text="Alunos Cadastrados:").pack(pady=(20,5))
        
        self.tree_alunos = ttk.Treeview(frame_alunos, columns=('ID', 'Nome'), 
                                       show='headings', height=8)
        self.tree_alunos.heading('ID', text='ID')
        self.tree_alunos.heading('Nome', text='Nome')
        self.tree_alunos.pack(pady=5, fill='x')
        
        # Botões
        frame_btn_alunos = ttk.Frame(frame_alunos)
        frame_btn_alunos.pack(pady=10)
        
        ttk.Button(frame_btn_alunos, text="Atualizar Lista", 
                  command=self.atualizar_alunos).pack(side='left', padx=5)
        ttk.Button(frame_btn_alunos, text="Excluir Selecionado", 
                  command=self.excluir_aluno).pack(side='left', padx=5)
        
        self.atualizar_alunos()
    
    def criar_aba_disciplinas(self, notebook):
        """Cria aba para gerenciar disciplinas"""
        frame_disc = ttk.Frame(notebook)
        notebook.add(frame_disc, text="Disciplinas")
        
        # Inserir disciplina
        ttk.Label(frame_disc, text="Nome da Disciplina:").pack(pady=5)
        self.entry_disciplina = ttk.Entry(frame_disc, width=30)
        self.entry_disciplina.pack(pady=5)
        
        ttk.Button(frame_disc, text="Inserir Disciplina", 
                  command=self.inserir_disciplina).pack(pady=5)
        
        # Lista de disciplinas
        ttk.Label(frame_disc, text="Disciplinas Cadastradas:").pack(pady=(20,5))
        
        self.tree_disciplinas = ttk.Treeview(frame_disc, columns=('ID', 'Nome'), 
                                           show='headings', height=8)
        self.tree_disciplinas.heading('ID', text='ID')
        self.tree_disciplinas.heading('Nome', text='Nome')
        self.tree_disciplinas.pack(pady=5, fill='x')
        
        # Botões
        frame_btn_disc = ttk.Frame(frame_disc)
        frame_btn_disc.pack(pady=10)
        
        ttk.Button(frame_btn_disc, text="Atualizar Lista", 
                  command=self.atualizar_disciplinas).pack(side='left', padx=5)
        ttk.Button(frame_btn_disc, text="Excluir Selecionado", 
                  command=self.excluir_disciplina).pack(side='left', padx=5)
        
        self.atualizar_disciplinas()
    
    def criar_aba_notas(self, notebook):
        """Cria aba para gerenciar notas"""
        frame_notas = ttk.Frame(notebook)
        notebook.add(frame_notas, text="Notas")
        
        # Frame para inserir nota
        frame_inserir = ttk.LabelFrame(frame_notas, text="Inserir Nova Nota")
        frame_inserir.pack(fill='x', padx=10, pady=5)
        
        # Campo para buscar aluno
        ttk.Label(frame_inserir, text="Aluno (ID ou Nome):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry_busca_aluno = ttk.Entry(frame_inserir, width=25)
        self.entry_busca_aluno.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame_inserir, text="Buscar", 
                  command=self.buscar_aluno).grid(row=0, column=2, padx=5, pady=5)
        
        # Campo para buscar disciplina
        ttk.Label(frame_inserir, text="Disciplina (ID ou Nome):").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entry_busca_disciplina = ttk.Entry(frame_inserir, width=25)
        self.entry_busca_disciplina.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(frame_inserir, text="Buscar", 
                  command=self.buscar_disciplina).grid(row=1, column=2, padx=5, pady=5)
        
        # Entry para nota
        ttk.Label(frame_inserir, text="Nota (0-10):").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.entry_nota = ttk.Entry(frame_inserir, width=10)
        self.entry_nota.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        # Botão inserir
        ttk.Button(frame_inserir, text="Inserir Nota", 
                  command=self.inserir_nota).grid(row=2, column=2, padx=5, pady=5)
        
        # Labels para mostrar seleções
        self.label_aluno_selecionado = ttk.Label(frame_inserir, text="Nenhum aluno selecionado", foreground="red")
        self.label_aluno_selecionado.grid(row=0, column=3, padx=5, pady=5, sticky='w')
        
        self.label_disciplina_selecionada = ttk.Label(frame_inserir, text="Nenhuma disciplina selecionada", foreground="red")
        self.label_disciplina_selecionada.grid(row=1, column=3, padx=5, pady=5, sticky='w')
        
        # Variáveis para armazenar IDs selecionados
        self.id_aluno_selecionado = None
        self.id_disciplina_selecionada = None
        
        # Lista de notas com ordenação clicável
        ttk.Label(frame_notas, text="Notas Cadastradas:").pack(pady=(20,5))
        
        self.tree_notas = ttk.Treeview(frame_notas, columns=('ID', 'Aluno', 'Disciplina', 'Nota'), 
                                      show='headings', height=10)
        
        # Cabeçalhos clicáveis para ordenação
        self.tree_notas.heading('ID', text='ID ↕', command=lambda: self.ordenar_notas('ID'))
        self.tree_notas.heading('Aluno', text='Aluno ↕', command=lambda: self.ordenar_notas('Aluno'))
        self.tree_notas.heading('Disciplina', text='Disciplina ↕', command=lambda: self.ordenar_notas('Disciplina'))
        self.tree_notas.heading('Nota', text='Nota ↕', command=lambda: self.ordenar_notas('Nota'))
        
        # Configurar largura das colunas
        self.tree_notas.column('ID', width=50)
        self.tree_notas.column('Aluno', width=150)
        self.tree_notas.column('Disciplina', width=150)
        self.tree_notas.column('Nota', width=80)
        
        self.tree_notas.pack(pady=5, fill='both', expand=True)
        
        # Botões para notas
        frame_btn_notas = ttk.Frame(frame_notas)
        frame_btn_notas.pack(pady=10)
        
        ttk.Button(frame_btn_notas, text="Atualizar Lista", 
                  command=self.atualizar_notas).pack(side='left', padx=5)
        ttk.Button(frame_btn_notas, text="Alterar Nota (Busca)", 
                  command=self.alterar_nota_busca).pack(side='left', padx=5)
        ttk.Button(frame_btn_notas, text="Excluir Nota (Busca)", 
                  command=self.excluir_nota_busca).pack(side='left', padx=5)
        
        # Variável para controle de ordenação
        self.ordem_notas = {'coluna': 'ID', 'reverso': False}
        
        # Inicializar dados
        self.atualizar_notas()

def main():
    root = tk.Tk()
    app = SistemaEscolarGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()