# 📚 Sistema de Gerenciamento Escolar

Um sistema completo de gerenciamento escolar desenvolvido em Python com SQLite para gerenciar alunos, disciplinas e notas de forma integrada.

## 🎯 Funcionalidades Principais

O sistema oferece **CRUD completo** (Create, Read, Update, Delete) para:
- **👨‍🎓 Alunos** - Cadastro e gerenciamento de estudantes
- **📖 Disciplinas** - Cadastro e gerenciamento de matérias
- **📊 Notas** - Sistema de avaliação vinculando alunos às disciplinas

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **SQLite3** - Banco de dados relacional
- **Arquitetura Modular** - Código organizado em módulos separados

## 📦 Estrutura do Projeto

```
trabalho python/
├── main.py              # Arquivo principal com menus
├── limpar_tela.py       # Função para limpeza de tela
├── inserir.py           # Funções de inserção (alunos/disciplinas)
├── listar.py            # Funções de listagem
├── alterar.py           # Funções de alteração
├── excluir.py           # Funções de exclusão
├── nota.py              # Funções específicas para notas
├── Banco.db             # Banco de dados SQLite (criado automaticamente)
└── README.md            # Este arquivo
```

## 🚀 Como Executar

1. **Clone ou baixe o projeto**
2. **Navegue até a pasta:**
   ```bash
   cd "C:\Users\tyago\Documents\trabalho python"
   ```
3. **Execute o programa:**
   ```bash
   python main.py
   ```

## 📊 Estrutura do Banco de Dados

### Tabela ALUNOS
- `ID` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- `NOME` (TEXT, NOT NULL)

### Tabela DISCIPLINAS
- `ID` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- `NOME` (TEXT, NOT NULL)

### Tabela NOTAS
- `ID` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- `ID_ALUNO` (INTEGER, FOREIGN KEY → ALUNOS.ID)
- `ID_DISCIPLINA` (INTEGER, FOREIGN KEY → DISCIPLINAS.ID)
- `NOTA` (REAL, NOT NULL, 0-10)

## 🎮 Como Usar o Sistema

### Menu Principal
```
==================================================
                SISTEMA ESCOLAR                 
==================================================

Opções disponíveis:            
    1. Inserir 
    2. Alterar
    3. Listar
    4. Excluir
    5. Sair
```

### Submenu por Categoria
Após escolher uma opção (1-4), você verá:
```
Opções disponíveis para [AÇÃO]:
    1. Aluno
    2. Disciplina
    3. Nota
    4. Voltar
```

## 📝 Funcionalidades Detalhadas

### 🔹 **1. INSERIR**

#### **1.1 Inserir Aluno**
- **Caminho:** Menu Principal → 1. Inserir → 1. Aluno
- **Função:** Cadastra novo aluno no sistema
- **Entrada:** Nome do aluno
- **Validação:** Nome não pode estar vazio
- **Resultado:** Aluno adicionado à tabela ALUNOS

#### **1.2 Inserir Disciplina**
- **Caminho:** Menu Principal → 1. Inserir → 2. Disciplina
- **Função:** Cadastra nova disciplina no sistema
- **Entrada:** Nome da disciplina
- **Validação:** Nome não pode estar vazio
- **Resultado:** Disciplina adicionada à tabela DISCIPLINAS

#### **1.3 Inserir Nota**
- **Caminho:** Menu Principal → 1. Inserir → 3. Nota
- **Função:** Cadastra nota vinculando aluno à disciplina
- **Processo:**
  1. Lista alunos disponíveis
  2. Usuário seleciona ID do aluno
  3. Lista disciplinas disponíveis
  4. Usuário seleciona ID da disciplina
  5. Usuário digita a nota (0-10)
- **Validações:** 
  - IDs devem existir
  - Nota deve estar entre 0 e 10
- **Resultado:** Nota adicionada à tabela NOTAS

### 🔹 **2. LISTAR**

#### **2.1 Listar Alunos**
- **Caminho:** Menu Principal → 3. Listar → 1. Aluno
- **Função:** Exibe todos os alunos cadastrados
- **Formato:**
  ```
  ID    NOME                          
  ----------------------------------------
  1     João Silva                    
  2     Maria Santos                  
  ```

#### **2.2 Listar Disciplinas**
- **Caminho:** Menu Principal → 3. Listar → 2. Disciplina
- **Função:** Exibe todas as disciplinas cadastradas
- **Formato:** Igual ao listar alunos

#### **2.3 Listar Notas**
- **Caminho:** Menu Principal → 3. Listar → 3. Nota
- **Função:** Exibe todas as notas com JOIN das tabelas
- **Formato:**
  ```
  ID    ALUNO               DISCIPLINA          NOTA 
  -------------------------------------------------------
  1     João Silva          Matemática          8.5  
  2     Maria Santos        Português           9.0  
  ```

### 🔹 **3. ALTERAR**

#### **3.1 Alterar Aluno**
- **Caminho:** Menu Principal → 2. Alterar → 1. Aluno
- **Função:** Modifica nome de aluno existente
- **Processo:**
  1. Lista todos os alunos
  2. Usuário digita ID do aluno
  3. Sistema mostra nome atual
  4. Usuário digita novo nome
- **Validações:** ID deve existir, nome não pode estar vazio

#### **3.2 Alterar Disciplina**
- **Caminho:** Menu Principal → 2. Alterar → 2. Disciplina
- **Função:** Modifica nome de disciplina existente
- **Processo:** Igual ao alterar aluno

#### **3.3 Alterar Nota**
- **Caminho:** Menu Principal → 2. Alterar → 3. Nota
- **Função:** Modifica nota de aluno em disciplina específica
- **Processo:**
  1. Lista alunos disponíveis
  2. Usuário seleciona ID do aluno
  3. Lista disciplinas disponíveis
  4. Usuário seleciona ID da disciplina
  5. Sistema mostra nota atual
  6. Usuário digita nova nota
- **Validações:** Aluno, disciplina e nota devem existir; nova nota entre 0-10

### 🔹 **4. EXCLUIR**

#### **4.1 Excluir Aluno**
- **Caminho:** Menu Principal → 4. Excluir → 1. Aluno
- **Função:** Remove aluno do sistema
- **Processo:**
  1. Lista todos os alunos
  2. Usuário digita ID do aluno
  3. Sistema mostra dados do aluno
  4. Usuário confirma digitando "SIM"
- **Segurança:** Confirmação obrigatória

#### **4.2 Excluir Disciplina**
- **Caminho:** Menu Principal → 4. Excluir → 2. Disciplina
- **Função:** Remove disciplina do sistema
- **Processo:** Igual ao excluir aluno

#### **4.3 Excluir Nota**
- **Caminho:** Menu Principal → 4. Excluir → 3. Nota
- **Função:** Remove nota específica de aluno/disciplina
- **Processo:**
  1. Lista alunos disponíveis
  2. Usuário seleciona ID do aluno
  3. Lista disciplinas disponíveis
  4. Usuário seleciona ID da disciplina
  5. Sistema mostra dados da nota
  6. Usuário confirma digitando "SIM"
- **Segurança:** Confirmação obrigatória

## 🔧 Recursos Técnicos

### **Validações Implementadas**
- ✅ Verificação de IDs existentes
- ✅ Validação de entrada de dados
- ✅ Notas limitadas entre 0 e 10
- ✅ Campos obrigatórios não podem estar vazios

### **Segurança**
- ✅ Confirmação para exclusões
- ✅ Tratamento de erros com try/except
- ✅ Uso de prepared statements (proteção SQL injection)
- ✅ Context manager para conexões de banco

### **Interface**
- ✅ Limpeza automática de tela
- ✅ Menus organizados e intuitivos
- ✅ Feedback visual para operações
- ✅ Formatação tabular para listagens

## 🎯 Fluxo de Uso Recomendado

1. **Primeiro:** Cadastre alunos (Inserir → Aluno)
2. **Segundo:** Cadastre disciplinas (Inserir → Disciplina)
3. **Terceiro:** Cadastre notas (Inserir → Nota)
4. **Depois:** Use as funções de listar, alterar e excluir conforme necessário

## 🚨 Observações Importantes

- **Dependências:** O sistema gerencia automaticamente as relações entre tabelas
- **Backup:** O arquivo `Banco.db` contém todos os dados
- **Portabilidade:** Funciona em Windows, Linux e macOS
- **Persistência:** Dados são salvos automaticamente no SQLite

## 👨‍💻 Desenvolvido por

Sistema desenvolvido como projeto educacional em Python, demonstrando conceitos de:
- Programação orientada a módulos
- Banco de dados relacional
- Interface de linha de comando
- CRUD completo
- Boas práticas de programação

---

**Versão:** 1.0  
**Linguagem:** Python 3.x  
**Banco:** SQLite3  
**Licença:** Educacional