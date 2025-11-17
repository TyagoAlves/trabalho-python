# 📤 Sistema Escolar - Funcionalidade de Exportação

Documentação completa da nova funcionalidade de exportação de dados em múltiplos formatos.

## 🚀 Como Acessar

```bash
python main.py
# Escolha opção 5: Exportar Dados
```

## 📊 Menu de Exportação

### **Interface Principal**
```
==================================================
                EXPORTAR DADOS                 
==================================================

Escolha o que exportar:
    1. Alunos
    2. Disciplinas  
    3. Notas
    4. Todos os dados
    5. Voltar
```

### **Seleção de Formato**
```
Exportar [TIPO] em qual formato?

    1. TXT (Texto formatado)
    2. CSV (Planilha)
    3. JSON (Dados estruturados)
    4. Voltar
```

---

## 📝 EXPORTAÇÃO TXT

### **Características**
- **Formato:** Texto formatado e legível
- **Codificação:** UTF-8 (suporte completo a acentos)
- **Layout:** Tabelas organizadas com cabeçalhos
- **Uso:** Relatórios, documentação, visualização

### **Exemplo de Saída - Alunos**
```
============================================================
SISTEMA ESCOLAR - EXPORTAÇÃO ALUNOS
Data/Hora: 15/12/2024 14:30:25
============================================================

LISTA DE ALUNOS
----------------------------------------
ID    NOME                          
----------------------------------------
1     João Silva                    
2     Maria Santos                  
3     Pedro Costa                   
```

### **Exemplo de Saída - Notas**
```
============================================================
SISTEMA ESCOLAR - EXPORTAÇÃO NOTAS
Data/Hora: 15/12/2024 14:30:25
============================================================

LISTA DE NOTAS
----------------------------------------------------------------------
ID    ALUNO               DISCIPLINA          NOTA      
----------------------------------------------------------------------
1     João Silva          Matemática          8.5       
2     Maria Santos        Português           9.0       
3     Pedro Costa         História            7.5       
```

### **Nomenclatura de Arquivos**
- **Padrão:** `{tipo}_{timestamp}.txt`
- **Exemplo:** `alunos_20241215_143025.txt`
- **Timestamp:** AAAAMMDD_HHMMSS

---

## 📊 EXPORTAÇÃO CSV

### **Características**
- **Formato:** Planilha compatível com Excel
- **Separador:** Ponto e vírgula (;) - padrão brasileiro
- **Codificação:** UTF-8
- **Compatibilidade:** Excel, LibreOffice, Google Sheets

### **Exemplo de Saída - Disciplinas**
```
ID;NOME
1;Matemática
2;Português
3;História
4;Ciências
```

### **Exemplo de Saída - Notas**
```
ID;ALUNO;DISCIPLINA;NOTA
1;João Silva;Matemática;8.5
2;Maria Santos;Português;9.0
3;Pedro Costa;História;7.5
```

### **Exemplo de Saída - Todos os Dados**
```
TABELA;ID;NOME/ALUNO;DISCIPLINA;NOTA
ALUNOS;1;João Silva;;
ALUNOS;2;Maria Santos;;
DISCIPLINAS;1;Matemática;;
DISCIPLINAS;2;Português;;
NOTAS;1;João Silva;Matemática;8.5
NOTAS;2;Maria Santos;Português;9.0
```

### **Como Abrir no Excel**
1. Abra o Excel
2. Vá em Dados → Obter Dados → De Arquivo → De Texto/CSV
3. Selecione o arquivo .csv
4. Configure separador como "Ponto e vírgula"
5. Clique em "Carregar"

---

## 🔗 EXPORTAÇÃO JSON

### **Características**
- **Formato:** Dados estruturados para APIs
- **Estrutura:** Objetos aninhados com metadados
- **Codificação:** UTF-8
- **Uso:** APIs, backup estruturado, integração entre sistemas

### **Exemplo de Saída - Alunos**
```json
{
  "sistema": "Sistema Escolar",
  "exportacao": {
    "data_hora": "15/12/2024 14:30:25",
    "tipo": "alunos"
  },
  "alunos": [
    {"id": 1, "nome": "João Silva"},
    {"id": 2, "nome": "Maria Santos"},
    {"id": 3, "nome": "Pedro Costa"}
  ]
}
```

### **Exemplo de Saída - Notas**
```json
{
  "sistema": "Sistema Escolar",
  "exportacao": {
    "data_hora": "15/12/2024 14:30:25",
    "tipo": "notas"
  },
  "notas": [
    {
      "id": 1,
      "aluno": {"id": 1, "nome": "João Silva"},
      "disciplina": {"id": 1, "nome": "Matemática"},
      "nota": 8.5
    },
    {
      "id": 2,
      "aluno": {"id": 2, "nome": "Maria Santos"},
      "disciplina": {"id": 2, "nome": "Português"},
      "nota": 9.0
    }
  ]
}
```

### **Exemplo de Saída - Todos os Dados**
```json
{
  "sistema": "Sistema Escolar",
  "exportacao": {
    "data_hora": "15/12/2024 14:30:25",
    "tipo": "todos"
  },
  "alunos": [
    {"id": 1, "nome": "João Silva"},
    {"id": 2, "nome": "Maria Santos"}
  ],
  "disciplinas": [
    {"id": 1, "nome": "Matemática"},
    {"id": 2, "nome": "Português"}
  ],
  "notas": [
    {
      "id": 1,
      "aluno": {"id": 1, "nome": "João Silva"},
      "disciplina": {"id": 1, "nome": "Matemática"},
      "nota": 8.5
    }
  ]
}
```

---

## 🔧 Recursos Técnicos

### **Nomenclatura Automática**
- **Padrão:** `{tipo}_{timestamp}.{extensão}`
- **Timestamp:** Formato AAAAMMDD_HHMMSS
- **Exemplos:**
  - `alunos_20241215_143025.txt`
  - `disciplinas_20241215_143025.csv`
  - `notas_20241215_143025.json`
  - `todos_20241215_143025.json`

### **Tratamento de Dados**
- **Ordenação:** Todos os dados são ordenados por ID
- **JOIN Automático:** Notas incluem nomes de alunos e disciplinas
- **Encoding UTF-8:** Suporte completo a caracteres especiais
- **Validação:** Tratamento de erros com try/except

### **Consultas SQL Utilizadas**

#### **Alunos e Disciplinas**
```sql
SELECT ID, NOME FROM ALUNOS ORDER BY ID
SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID
```

#### **Notas (com JOIN)**
```sql
SELECT n.ID, a.NOME, d.NOME, n.NOTA 
FROM NOTAS n 
JOIN ALUNOS a ON n.ID_ALUNO = a.ID 
JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID 
ORDER BY n.ID
```

#### **Notas JSON (com IDs)**
```sql
SELECT n.ID, n.ID_ALUNO, a.NOME, n.ID_DISCIPLINA, d.NOME, n.NOTA 
FROM NOTAS n 
JOIN ALUNOS a ON n.ID_ALUNO = a.ID 
JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID 
ORDER BY n.ID
```

### **Feedback Visual**
- **✅ Sucesso:** "Arquivo 'nome.ext' criado com sucesso!"
- **❌ Erro:** "Erro ao criar arquivo: [detalhes]"
- **💡 Dicas específicas por formato:**
  - **CSV:** "Abra no Excel usando separador ';'"
  - **JSON:** "Formato estruturado para APIs e sistemas"

---

## 🎯 Casos de Uso

### **📝 TXT - Relatórios**
- Relatórios para impressão
- Documentação de dados
- Visualização rápida
- Backup legível

### **📊 CSV - Análise de Dados**
- Importação para Excel
- Análise estatística
- Gráficos e tabelas dinâmicas
- Compartilhamento com outros sistemas

### **🔗 JSON - Integração**
- APIs REST
- Backup estruturado
- Integração entre sistemas
- Processamento automatizado

### **📦 Todos os Dados - Backup Completo**
- Backup completo do sistema
- Migração de dados
- Auditoria completa
- Arquivo único com tudo

---

## 🚀 Fluxo de Uso

### **Passo a Passo**
1. Execute `python main.py`
2. Escolha opção **5. Exportar Dados**
3. Selecione o tipo de dados (1-4)
4. Escolha o formato (TXT/CSV/JSON)
5. Aguarde confirmação de criação
6. Arquivo salvo na pasta do projeto

### **Exemplo Prático**
```
Menu Principal → 5. Exportar Dados
↓
Escolher Dados → 3. Notas
↓
Escolher Formato → 2. CSV
↓
✅ Arquivo 'notas_20241215_143025.csv' criado com sucesso!
💡 Abra no Excel usando separador ';' (ponto e vírgula)
```

---

## 🔍 Estrutura do Código

### **Arquivo: exportar.py**
```python
# Funções principais:
exportar_dados(cursor, conn)     # Menu principal
escolher_formato(tipo, cursor)   # Seleção de formato
exportar_txt(tipo, cursor)       # Exportação TXT
exportar_csv(tipo, cursor)       # Exportação CSV
exportar_json(tipo, cursor)      # Exportação JSON
```

### **Integração com main.py**
```python
from exportar import exportar_dados

# Nova opção no menu:
case "5":
    exportar_dados(cursor, conn)
```

---

## 📋 Validações e Segurança

### **Tratamento de Erros**
- **Try/Except:** Captura erros de escrita
- **Validação de Dados:** Verifica dados antes da exportação
- **Feedback Claro:** Mensagens específicas para cada erro

### **Segurança de Dados**
- **Sem Exposição:** Não expõe dados sensíveis
- **Encoding Seguro:** UTF-8 previne corrupção
- **Validação SQL:** Prepared statements implícitos

---

**Funcionalidade implementada com:** Python 3.x + SQLite3 + JSON + CSV  
**Compatibilidade:** Windows, Linux, macOS  
**Formatos suportados:** TXT, CSV, JSON