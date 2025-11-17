# 🖥️ Sistema Escolar - Interface Gráfica (Tkinter)

Interface gráfica moderna desenvolvida em Python com Tkinter para gerenciamento escolar completo.

## 🚀 Como Executar

```bash
python launcher.py
# Escolha opção 2: Interface Gráfica
```

## 📊 Estrutura da Interface

### **Sistema de Abas**
- **Aba Alunos** - Gerenciamento completo de estudantes
- **Aba Disciplinas** - Gerenciamento de matérias
- **Aba Notas** - Sistema avançado de avaliações

---

## 👨🎓 ABA ALUNOS

### **Componentes da Interface**
```
┌─ Nome do Aluno: [_____________]
├─ [Inserir Aluno]
├─ Alunos Cadastrados:
├─ ┌─────────────────────────┐
├─ │ ID │ Nome               │
├─ │ 1  │ João Silva         │
├─ │ 2  │ Maria Santos       │
├─ └─────────────────────────┘
└─ [Atualizar Lista] [Excluir Selecionado]
```

### **Funcionalidades**

#### **🔹 inserir_aluno()**
- **Entrada:** Campo de texto `entry_aluno`
- **Validação:** Nome não pode estar vazio
- **Processo:**
  1. Captura texto do campo
  2. Remove espaços em branco
  3. Valida se não está vazio
  4. Executa SQL: `INSERT INTO ALUNOS (NOME) VALUES (?)`
  5. Confirma transação
  6. Limpa campo
  7. Atualiza lista automaticamente
- **Feedback:** MessageBox de sucesso/erro

#### **🔹 atualizar_alunos()**
- **Função:** Recarrega dados na TreeView
- **Processo:**
  1. Limpa todos os itens da árvore
  2. Executa SQL: `SELECT ID, NOME FROM ALUNOS ORDER BY ID`
  3. Insere cada linha na TreeView
- **Chamada:** Automática após inserir/excluir

#### **🔹 excluir_aluno()**
- **Entrada:** Item selecionado na TreeView
- **Validação:** Verifica se há seleção
- **Processo:**
  1. Captura item selecionado
  2. Extrai ID e nome do aluno
  3. Exibe confirmação com nome
  4. Executa SQL: `DELETE FROM ALUNOS WHERE ID = ?`
  5. Atualiza lista
- **Segurança:** Confirmação obrigatória via MessageBox

---

## 📖 ABA DISCIPLINAS

### **Componentes da Interface**
```
┌─ Nome da Disciplina: [_____________]
├─ [Inserir Disciplina]
├─ Disciplinas Cadastradas:
├─ ┌─────────────────────────┐
├─ │ ID │ Nome               │
├─ │ 1  │ Matemática         │
├─ │ 2  │ Português          │
├─ └─────────────────────────┘
└─ [Atualizar Lista] [Excluir Selecionado]
```

### **Funcionalidades**

#### **🔹 inserir_disciplina()**
- **Entrada:** Campo `entry_disciplina`
- **Validação:** Nome obrigatório
- **SQL:** `INSERT INTO DISCIPLINAS (NOME) VALUES (?)`
- **Comportamento:** Idêntico ao inserir_aluno()

#### **🔹 atualizar_disciplinas()**
- **SQL:** `SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID`
- **Comportamento:** Idêntico ao atualizar_alunos()

#### **🔹 excluir_disciplina()**
- **SQL:** `DELETE FROM DISCIPLINAS WHERE ID = ?`
- **Comportamento:** Idêntico ao excluir_aluno()

---

## 📊 ABA NOTAS (Funcionalidade Avançada)

### **Componentes da Interface**
```
┌─ Inserir Nova Nota ─────────────────────────┐
├─ Aluno (ID ou Nome): [_______] [Buscar] Status
├─ Disciplina (ID ou Nome): [___] [Buscar] Status  
├─ Nota (0-10): [___] [Inserir Nota]
└─────────────────────────────────────────────┘

┌─ Notas Cadastradas: ────────────────────────┐
├─ ID↕ │ Aluno↕        │ Disciplina↕   │ Nota↕
├─ 1   │ João Silva    │ Matemática    │ 8.5
├─ 2   │ Maria Santos  │ Português     │ 9.0
└─────────────────────────────────────────────┘

[Atualizar Lista] [Alterar Nota] [Excluir Nota]
```

### **Sistema de Busca Inteligente**

#### **🔹 buscar_aluno()**
- **Entrada:** Campo `entry_busca_aluno`
- **Tipos de busca:**
  - **Por ID:** Se entrada for numérica
  - **Por Nome:** Busca parcial com LIKE
- **SQL Dinâmico:**
  ```sql
  -- Se for número:
  SELECT ID, NOME FROM ALUNOS WHERE ID = ?
  
  -- Se for texto:
  SELECT ID, NOME FROM ALUNOS WHERE NOME LIKE %?%
  ```
- **Feedback Visual:**
  - **Encontrado:** Label verde "Selecionado: Nome"
  - **Não encontrado:** MessageBox informativo
- **Armazenamento:** `self.id_aluno_selecionado`

#### **🔹 buscar_disciplina()**
- **Comportamento:** Idêntico ao buscar_aluno()
- **Armazenamento:** `self.id_disciplina_selecionada`

### **Sistema de Inserção de Notas**

#### **🔹 inserir_nota()**
- **Pré-requisitos:** Aluno E disciplina selecionados
- **Validações:**
  1. Verifica seleções obrigatórias
  2. Converte nota para float
  3. Valida range 0-10
- **SQL:** `INSERT INTO NOTAS (ID_ALUNO, ID_DISCIPLINA, NOTA) VALUES (?, ?, ?)`
- **Processo:**
  1. Valida pré-requisitos
  2. Converte e valida nota
  3. Insere no banco
  4. Limpa campo nota
  5. Atualiza lista

### **Sistema de Ordenação Clicável**

#### **🔹 ordenar_notas(coluna)**
- **Entrada:** Nome da coluna clicada
- **Controle de Estado:** `self.ordem_notas = {'coluna': 'ID', 'reverso': False}`
- **Lógica:**
  ```python
  if mesma_coluna:
      inverte_ordem()
  else:
      nova_coluna_ascendente()
  ```
- **Mapeamento de Colunas:**
  ```python
  coluna_map = {
      'ID': 'n.ID',
      'Aluno': 'a.NOME', 
      'Disciplina': 'd.NOME',
      'Nota': 'n.NOTA'
  }
  ```

#### **🔹 atualizar_notas()**
- **SQL Complexo com JOIN:**
  ```sql
  SELECT n.ID, a.NOME, d.NOME, n.NOTA 
  FROM NOTAS n 
  JOIN ALUNOS a ON n.ID_ALUNO = a.ID 
  JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID
  ORDER BY {coluna} {ASC/DESC}
  ```
- **Ordenação Dinâmica:** Aplica ordenação baseada no estado atual

### **Sistema de Alteração Avançada**

#### **🔹 alterar_nota_busca()**
- **Interface:** Janela popup (Toplevel)
- **Componentes:**
  ```
  ┌─ Alterar Nota ──────────────┐
  ├─ Buscar Aluno: [__________] │
  ├─ Buscar Disciplina: [____] │
  ├─ Nova Nota: [___]          │
  ├─ [Alterar]                 │
  └─────────────────────────────┘
  ```
- **Processo:**
  1. Busca aluno (ID ou nome)
  2. Busca disciplina (ID ou nome)
  3. Valida nova nota (0-10)
  4. Localiza registro existente
  5. Executa UPDATE
- **SQL:** `UPDATE NOTAS SET NOTA = ? WHERE ID_ALUNO = ? AND ID_DISCIPLINA = ?`
- **Validação:** Verifica se registro foi afetado

#### **🔹 excluir_nota_busca()**
- **Interface:** Janela popup similar
- **Processo:**
  1. Busca aluno e disciplina
  2. Confirmação obrigatória
  3. Executa DELETE
- **SQL:** `DELETE FROM NOTAS WHERE ID_ALUNO = ? AND ID_DISCIPLINA = ?`

---

## 🔧 Recursos Técnicos Avançados

### **Gerenciamento de Conexão**
```python
self.conn = sqlite3.connect('Banco.db')
self.cursor = self.conn.cursor()
```

### **Context Management**
- **Commits automáticos** após operações
- **Rollback implícito** em caso de erro
- **Tratamento de exceções** com try/except

### **Componentes Tkinter Utilizados**

#### **TreeView Avançada**
```python
self.tree_notas = ttk.Treeview(
    columns=('ID', 'Aluno', 'Disciplina', 'Nota'),
    show='headings',
    height=10
)

# Cabeçalhos clicáveis
self.tree_notas.heading('ID', text='ID ↕', 
                       command=lambda: self.ordenar_notas('ID'))
```

#### **Labels Dinâmicos**
```python
self.label_aluno_selecionado = ttk.Label(
    text="Nenhum aluno selecionado", 
    foreground="red"
)

# Atualização dinâmica
self.label_aluno_selecionado.config(
    text=f"Selecionado: {nome}", 
    foreground="green"
)
```

#### **Janelas Popup (Toplevel)**
```python
janela = tk.Toplevel(self.root)
janela.title("Alterar Nota")
janela.geometry("400x300")
```

### **Validações Implementadas**

#### **Validação de Entrada**
```python
# Campos obrigatórios
if not nome.strip():
    messagebox.showerror("Erro", "Nome não pode estar vazio!")

# Range de notas
if not (0 <= nota <= 10):
    messagebox.showerror("Erro", "Nota deve estar entre 0 e 10!")

# Conversão segura
try:
    nota = float(self.entry_nota.get())
except ValueError:
    messagebox.showerror("Erro", "Digite uma nota válida!")
```

#### **Validação de Seleção**
```python
# TreeView
selected = self.tree_alunos.selection()
if not selected:
    messagebox.showwarning("Aviso", "Selecione um item!")

# Busca obrigatória
if not self.id_aluno_selecionado:
    messagebox.showwarning("Aviso", "Selecione aluno primeiro!")
```

### **Feedback Visual Avançado**

#### **MessageBox Tipificado**
- **showinfo()** - Operações bem-sucedidas
- **showerror()** - Erros de validação/sistema
- **showwarning()** - Avisos ao usuário
- **askyesno()** - Confirmações de exclusão

#### **Labels Coloridos**
- **Verde** - Seleção confirmada
- **Vermelho** - Nenhuma seleção

#### **Símbolos Visuais**
- **↕** - Indica colunas ordenáveis
- **Larguras personalizadas** nas colunas

---

## 🎯 Fluxo de Uso Recomendado

### **1. Preparação**
1. Execute `python launcher.py`
2. Escolha opção 2 (Interface Gráfica)

### **2. Cadastro Inicial**
1. **Aba Alunos** → Cadastre estudantes
2. **Aba Disciplinas** → Cadastre matérias

### **3. Gerenciamento de Notas**
1. **Aba Notas** → Busque aluno
2. Busque disciplina
3. Digite nota (0-10)
4. Clique "Inserir Nota"

### **4. Funcionalidades Avançadas**
- **Ordenação:** Clique nos cabeçalhos ↕
- **Alteração:** Use "Alterar Nota (Busca)"
- **Exclusão:** Use "Excluir Nota (Busca)"

---

## 🚨 Características Técnicas

### **Performance**
- **Lazy Loading** - Dados carregados sob demanda
- **Índices automáticos** - SQLite otimizado
- **Conexão persistente** - Uma conexão por sessão

### **Usabilidade**
- **Busca inteligente** - ID ou nome parcial
- **Feedback imediato** - Labels coloridos
- **Confirmações** - Evita exclusões acidentais
- **Limpeza automática** - Campos limpos após operações

### **Arquitetura**
- **Separação de responsabilidades** - UI/Lógica/Dados
- **Reutilização de código** - Métodos similares
- **Tratamento de erros** - Try/except abrangente

---

**Desenvolvido com:** Python 3.x + Tkinter + SQLite3  
**Arquitetura:** MVC Pattern  
**Interface:** Desktop GUI Nativa