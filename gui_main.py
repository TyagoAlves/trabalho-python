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
    
    # MÉTODOS PARA ALUNOS
    def inserir_aluno(self):
        nome = self.entry_aluno.get().strip()
        if not nome:
            messagebox.showerror("Erro", "Nome não pode estar vazio!")
            return
        
        try:
            self.cursor.execute("INSERT INTO ALUNOS (NOME) VALUES (?)", (nome,))
            self.conn.commit()
            messagebox.showinfo("Sucesso", f"Aluno '{nome}' inserido com sucesso!")
            self.entry_aluno.delete(0, tk.END)
            self.atualizar_alunos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao inserir aluno: {e}")
    
    def atualizar_alunos(self):
        for item in self.tree_alunos.get_children():
            self.tree_alunos.delete(item)
        
        self.cursor.execute("SELECT ID, NOME FROM ALUNOS ORDER BY ID")
        for row in self.cursor.fetchall():
            self.tree_alunos.insert('', 'end', values=row)
    
    def excluir_aluno(self):
        selected = self.tree_alunos.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um aluno para excluir!")
            return
        
        item = self.tree_alunos.item(selected[0])
        id_aluno = item['values'][0]
        nome = item['values'][1]
        
        if messagebox.askyesno("Confirmar", f"Excluir aluno '{nome}'?"):
            try:
                self.cursor.execute("DELETE FROM ALUNOS WHERE ID = ?", (id_aluno,))
                self.conn.commit()
                messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!")
                self.atualizar_alunos()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir aluno: {e}")
    
    # MÉTODOS PARA DISCIPLINAS
    def inserir_disciplina(self):
        nome = self.entry_disciplina.get().strip()
        if not nome:
            messagebox.showerror("Erro", "Nome não pode estar vazio!")
            return
        
        try:
            self.cursor.execute("INSERT INTO DISCIPLINAS (NOME) VALUES (?)", (nome,))
            self.conn.commit()
            messagebox.showinfo("Sucesso", f"Disciplina '{nome}' inserida com sucesso!")
            self.entry_disciplina.delete(0, tk.END)
            self.atualizar_disciplinas()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao inserir disciplina: {e}")
    
    def atualizar_disciplinas(self):
        for item in self.tree_disciplinas.get_children():
            self.tree_disciplinas.delete(item)
        
        self.cursor.execute("SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID")
        for row in self.cursor.fetchall():
            self.tree_disciplinas.insert('', 'end', values=row)
    
    def excluir_disciplina(self):
        selected = self.tree_disciplinas.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione uma disciplina para excluir!")
            return
        
        item = self.tree_disciplinas.item(selected[0])
        id_disciplina = item['values'][0]
        nome = item['values'][1]
        
        if messagebox.askyesno("Confirmar", f"Excluir disciplina '{nome}'?"):
            try:
                self.cursor.execute("DELETE FROM DISCIPLINAS WHERE ID = ?", (id_disciplina,))
                self.conn.commit()
                messagebox.showinfo("Sucesso", "Disciplina excluída com sucesso!")
                self.atualizar_disciplinas()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir disciplina: {e}")
    
    # MÉTODOS PARA NOTAS
    def buscar_aluno(self):
        busca = self.entry_busca_aluno.get().strip()
        if not busca:
            messagebox.showwarning("Aviso", "Digite ID ou nome do aluno!")
            return
        
        try:
            if busca.isdigit():
                self.cursor.execute("SELECT ID, NOME FROM ALUNOS WHERE ID = ?", (int(busca),))
            else:
                self.cursor.execute("SELECT ID, NOME FROM ALUNOS WHERE NOME LIKE ?", (f"%{busca}%",))
            
            resultado = self.cursor.fetchone()
            if resultado:
                self.id_aluno_selecionado = resultado[0]
                self.label_aluno_selecionado.config(text=f"Selecionado: {resultado[1]}", foreground="green")
            else:
                messagebox.showinfo("Não encontrado", "Aluno não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na busca: {e}")
    
    def buscar_disciplina(self):
        busca = self.entry_busca_disciplina.get().strip()
        if not busca:
            messagebox.showwarning("Aviso", "Digite ID ou nome da disciplina!")
            return
        
        try:
            if busca.isdigit():
                self.cursor.execute("SELECT ID, NOME FROM DISCIPLINAS WHERE ID = ?", (int(busca),))
            else:
                self.cursor.execute("SELECT ID, NOME FROM DISCIPLINAS WHERE NOME LIKE ?", (f"%{busca}%",))
            
            resultado = self.cursor.fetchone()
            if resultado:
                self.id_disciplina_selecionada = resultado[0]
                self.label_disciplina_selecionada.config(text=f"Selecionada: {resultado[1]}", foreground="green")
            else:
                messagebox.showinfo("Não encontrado", "Disciplina não encontrada!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na busca: {e}")
    
    def inserir_nota(self):
        if not self.id_aluno_selecionado or not self.id_disciplina_selecionada:
            messagebox.showwarning("Aviso", "Selecione aluno e disciplina primeiro!")
            return
        
        try:
            nota = float(self.entry_nota.get())
            if not (0 <= nota <= 10):
                messagebox.showerror("Erro", "Nota deve estar entre 0 e 10!")
                return
        except ValueError:
            messagebox.showerror("Erro", "Digite uma nota válida!")
            return
        
        try:
            self.cursor.execute("INSERT INTO NOTAS (ID_ALUNO, ID_DISCIPLINA, NOTA) VALUES (?, ?, ?)",
                              (self.id_aluno_selecionado, self.id_disciplina_selecionada, nota))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Nota inserida com sucesso!")
            self.entry_nota.delete(0, tk.END)
            self.atualizar_notas()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao inserir nota: {e}")
    
    def atualizar_notas(self):
        for item in self.tree_notas.get_children():
            self.tree_notas.delete(item)
        
        sql = """SELECT n.ID, a.NOME, d.NOME, n.NOTA 
                 FROM NOTAS n 
                 JOIN ALUNOS a ON n.ID_ALUNO = a.ID 
                 JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID"""
        
        # Aplicar ordenação
        coluna_map = {'ID': 'n.ID', 'Aluno': 'a.NOME', 'Disciplina': 'd.NOME', 'Nota': 'n.NOTA'}
        coluna_sql = coluna_map.get(self.ordem_notas['coluna'], 'n.ID')
        ordem = 'DESC' if self.ordem_notas['reverso'] else 'ASC'
        sql += f" ORDER BY {coluna_sql} {ordem}"
        
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            self.tree_notas.insert('', 'end', values=row)
    
    def ordenar_notas(self, coluna):
        if self.ordem_notas['coluna'] == coluna:
            self.ordem_notas['reverso'] = not self.ordem_notas['reverso']
        else:
            self.ordem_notas['coluna'] = coluna
            self.ordem_notas['reverso'] = False
        
        self.atualizar_notas()
    
    def alterar_nota_busca(self):
        # Janela para buscar e alterar nota
        janela = tk.Toplevel(self.root)
        janela.title("Alterar Nota")
        janela.geometry("400x300")
        
        ttk.Label(janela, text="Buscar Aluno (ID ou Nome):").pack(pady=5)
        entry_aluno = ttk.Entry(janela, width=30)
        entry_aluno.pack(pady=5)
        
        ttk.Label(janela, text="Buscar Disciplina (ID ou Nome):").pack(pady=5)
        entry_disciplina = ttk.Entry(janela, width=30)
        entry_disciplina.pack(pady=5)
        
        ttk.Label(janela, text="Nova Nota (0-10):").pack(pady=5)
        entry_nova_nota = ttk.Entry(janela, width=10)
        entry_nova_nota.pack(pady=5)
        
        def alterar():
            # Implementação simplificada - busca e altera
            try:
                busca_aluno = entry_aluno.get().strip()
                busca_disc = entry_disciplina.get().strip()
                nova_nota = float(entry_nova_nota.get())
                
                if not (0 <= nova_nota <= 10):
                    messagebox.showerror("Erro", "Nota deve estar entre 0 e 10!")
                    return
                
                # Buscar IDs
                if busca_aluno.isdigit():
                    self.cursor.execute("SELECT ID FROM ALUNOS WHERE ID = ?", (int(busca_aluno),))
                else:
                    self.cursor.execute("SELECT ID FROM ALUNOS WHERE NOME LIKE ?", (f"%{busca_aluno}%",))
                aluno_result = self.cursor.fetchone()
                
                if busca_disc.isdigit():
                    self.cursor.execute("SELECT ID FROM DISCIPLINAS WHERE ID = ?", (int(busca_disc),))
                else:
                    self.cursor.execute("SELECT ID FROM DISCIPLINAS WHERE NOME LIKE ?", (f"%{busca_disc}%",))
                disc_result = self.cursor.fetchone()
                
                if not aluno_result or not disc_result:
                    messagebox.showerror("Erro", "Aluno ou disciplina não encontrados!")
                    return
                
                # Alterar nota
                self.cursor.execute("UPDATE NOTAS SET NOTA = ? WHERE ID_ALUNO = ? AND ID_DISCIPLINA = ?",
                                  (nova_nota, aluno_result[0], disc_result[0]))
                
                if self.cursor.rowcount > 0:
                    self.conn.commit()
                    messagebox.showinfo("Sucesso", "Nota alterada com sucesso!")
                    janela.destroy()
                    self.atualizar_notas()
                else:
                    messagebox.showwarning("Aviso", "Nota não encontrada para este aluno/disciplina!")
                    
            except ValueError:
                messagebox.showerror("Erro", "Digite uma nota válida!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao alterar nota: {e}")
        
        ttk.Button(janela, text="Alterar", command=alterar).pack(pady=20)
    
    def excluir_nota_busca(self):
        # Janela para buscar e excluir nota
        janela = tk.Toplevel(self.root)
        janela.title("Excluir Nota")
        janela.geometry("400x250")
        
        ttk.Label(janela, text="Buscar Aluno (ID ou Nome):").pack(pady=5)
        entry_aluno = ttk.Entry(janela, width=30)
        entry_aluno.pack(pady=5)
        
        ttk.Label(janela, text="Buscar Disciplina (ID ou Nome):").pack(pady=5)
        entry_disciplina = ttk.Entry(janela, width=30)
        entry_disciplina.pack(pady=5)
        
        def excluir():
            try:
                busca_aluno = entry_aluno.get().strip()
                busca_disc = entry_disciplina.get().strip()
                
                # Buscar IDs
                if busca_aluno.isdigit():
                    self.cursor.execute("SELECT ID FROM ALUNOS WHERE ID = ?", (int(busca_aluno),))
                else:
                    self.cursor.execute("SELECT ID FROM ALUNOS WHERE NOME LIKE ?", (f"%{busca_aluno}%",))
                aluno_result = self.cursor.fetchone()
                
                if busca_disc.isdigit():
                    self.cursor.execute("SELECT ID FROM DISCIPLINAS WHERE ID = ?", (int(busca_disc),))
                else:
                    self.cursor.execute("SELECT ID FROM DISCIPLINAS WHERE NOME LIKE ?", (f"%{busca_disc}%",))
                disc_result = self.cursor.fetchone()
                
                if not aluno_result or not disc_result:
                    messagebox.showerror("Erro", "Aluno ou disciplina não encontrados!")
                    return
                
                if messagebox.askyesno("Confirmar", "Excluir esta nota?"):
                    self.cursor.execute("DELETE FROM NOTAS WHERE ID_ALUNO = ? AND ID_DISCIPLINA = ?",
                                      (aluno_result[0], disc_result[0]))
                    
                    if self.cursor.rowcount > 0:
                        self.conn.commit()
                        messagebox.showinfo("Sucesso", "Nota excluída com sucesso!")
                        janela.destroy()
                        self.atualizar_notas()
                    else:
                        messagebox.showwarning("Aviso", "Nota não encontrada para este aluno/disciplina!")
                        
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir nota: {e}")
        
        ttk.Button(janela, text="Excluir", command=excluir).pack(pady=20)

def main():
    root = tk.Tk()
    app = SistemaEscolarGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()