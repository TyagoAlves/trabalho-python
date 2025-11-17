import sqlite3
import json
import csv
from datetime import datetime
from limpar_tela import limpar_tela

def exportar_dados(cursor, conn):
    """Menu principal para exportação de dados"""
    limpar_tela()
    print("=" * 50)
    print("EXPORTAR DADOS".center(50))
    print("=" * 50)
    
    print("""
Escolha o que exportar:
    1. Alunos
    2. Disciplinas  
    3. Notas
    4. Todos os dados
    5. Voltar
    """)
    
    opcao = input("Digite uma opção: ")
    
    match opcao:
        case "1":
            escolher_formato("alunos", cursor)
        case "2":
            escolher_formato("disciplinas", cursor)
        case "3":
            escolher_formato("notas", cursor)
        case "4":
            escolher_formato("todos", cursor)
        case "5":
            return
        case _:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")
            exportar_dados(cursor, conn)

def escolher_formato(tipo_dados, cursor):
    """Escolhe o formato de exportação"""
    limpar_tela()
    print(f"Exportar {tipo_dados.upper()} em qual formato?")
    print("""
    1. TXT (Texto formatado)
    2. CSV (Planilha)
    3. JSON (Dados estruturados)
    4. Voltar
    """)
    
    formato = input("Digite uma opção: ")
    
    match formato:
        case "1":
            exportar_txt(tipo_dados, cursor)
        case "2":
            exportar_csv(tipo_dados, cursor)
        case "3":
            exportar_json(tipo_dados, cursor)
        case "4":
            return
        case _:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")
            escolher_formato(tipo_dados, cursor)

def exportar_txt(tipo_dados, cursor):
    """Exporta dados em formato TXT"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{tipo_dados}_{timestamp}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write(f"SISTEMA ESCOLAR - EXPORTAÇÃO {tipo_dados.upper()}\n")
            f.write(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")
            
            if tipo_dados == "alunos":
                cursor.execute("SELECT ID, NOME FROM ALUNOS ORDER BY ID")
                f.write("LISTA DE ALUNOS\n")
                f.write("-" * 40 + "\n")
                f.write(f"{'ID':<5} {'NOME':<30}\n")
                f.write("-" * 40 + "\n")
                for row in cursor.fetchall():
                    f.write(f"{row[0]:<5} {row[1]:<30}\n")
                    
            elif tipo_dados == "disciplinas":
                cursor.execute("SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID")
                f.write("LISTA DE DISCIPLINAS\n")
                f.write("-" * 40 + "\n")
                f.write(f"{'ID':<5} {'NOME':<30}\n")
                f.write("-" * 40 + "\n")
                for row in cursor.fetchall():
                    f.write(f"{row[0]:<5} {row[1]:<30}\n")
                    
            elif tipo_dados == "notas":
                cursor.execute("""
                    SELECT n.ID, a.NOME, d.NOME, n.NOTA 
                    FROM NOTAS n 
                    JOIN ALUNOS a ON n.ID_ALUNO = a.ID 
                    JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID 
                    ORDER BY n.ID
                """)
                f.write("LISTA DE NOTAS\n")
                f.write("-" * 70 + "\n")
                f.write(f"{'ID':<5} {'ALUNO':<20} {'DISCIPLINA':<20} {'NOTA':<10}\n")
                f.write("-" * 70 + "\n")
                for row in cursor.fetchall():
                    f.write(f"{row[0]:<5} {row[1]:<20} {row[2]:<20} {row[3]:<10}\n")
                    
            elif tipo_dados == "todos":
                # Alunos
                cursor.execute("SELECT ID, NOME FROM ALUNOS ORDER BY ID")
                f.write("ALUNOS\n")
                f.write("-" * 40 + "\n")
                for row in cursor.fetchall():
                    f.write(f"ID: {row[0]} - Nome: {row[1]}\n")
                
                f.write("\n" + "=" * 60 + "\n\n")
                
                # Disciplinas
                cursor.execute("SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID")
                f.write("DISCIPLINAS\n")
                f.write("-" * 40 + "\n")
                for row in cursor.fetchall():
                    f.write(f"ID: {row[0]} - Nome: {row[1]}\n")
                
                f.write("\n" + "=" * 60 + "\n\n")
                
                # Notas
                cursor.execute("""
                    SELECT n.ID, a.NOME, d.NOME, n.NOTA 
                    FROM NOTAS n 
                    JOIN ALUNOS a ON n.ID_ALUNO = a.ID 
                    JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID 
                    ORDER BY n.ID
                """)
                f.write("NOTAS\n")
                f.write("-" * 70 + "\n")
                for row in cursor.fetchall():
                    f.write(f"ID: {row[0]} - Aluno: {row[1]} - Disciplina: {row[2]} - Nota: {row[3]}\n")
        
        print(f"✅ Arquivo '{filename}' criado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao criar arquivo: {e}")
    
    input("Pressione Enter para continuar...")

def exportar_csv(tipo_dados, cursor):
    """Exporta dados em formato CSV"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{tipo_dados}_{timestamp}.csv"
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            
            if tipo_dados == "alunos":
                writer.writerow(['ID', 'NOME'])
                cursor.execute("SELECT ID, NOME FROM ALUNOS ORDER BY ID")
                writer.writerows(cursor.fetchall())
                
            elif tipo_dados == "disciplinas":
                writer.writerow(['ID', 'NOME'])
                cursor.execute("SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID")
                writer.writerows(cursor.fetchall())
                
            elif tipo_dados == "notas":
                writer.writerow(['ID', 'ALUNO', 'DISCIPLINA', 'NOTA'])
                cursor.execute("""
                    SELECT n.ID, a.NOME, d.NOME, n.NOTA 
                    FROM NOTAS n 
                    JOIN ALUNOS a ON n.ID_ALUNO = a.ID 
                    JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID 
                    ORDER BY n.ID
                """)
                writer.writerows(cursor.fetchall())
                
            elif tipo_dados == "todos":
                # Criar arquivo com múltiplas seções
                writer.writerow(['TABELA', 'ID', 'NOME/ALUNO', 'DISCIPLINA', 'NOTA'])
                
                cursor.execute("SELECT ID, NOME FROM ALUNOS ORDER BY ID")
                for row in cursor.fetchall():
                    writer.writerow(['ALUNOS', row[0], row[1], '', ''])
                
                cursor.execute("SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID")
                for row in cursor.fetchall():
                    writer.writerow(['DISCIPLINAS', row[0], row[1], '', ''])
                
                cursor.execute("""
                    SELECT n.ID, a.NOME, d.NOME, n.NOTA 
                    FROM NOTAS n 
                    JOIN ALUNOS a ON n.ID_ALUNO = a.ID 
                    JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID 
                    ORDER BY n.ID
                """)
                for row in cursor.fetchall():
                    writer.writerow(['NOTAS', row[0], row[1], row[2], row[3]])
        
        print(f"✅ Arquivo '{filename}' criado com sucesso!")
        print("💡 Abra no Excel usando separador ';' (ponto e vírgula)")
        
    except Exception as e:
        print(f"❌ Erro ao criar arquivo: {e}")
    
    input("Pressione Enter para continuar...")

def exportar_json(tipo_dados, cursor):
    """Exporta dados em formato JSON"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{tipo_dados}_{timestamp}.json"
    
    try:
        data = {
            "sistema": "Sistema Escolar",
            "exportacao": {
                "data_hora": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                "tipo": tipo_dados
            }
        }
        
        if tipo_dados == "alunos":
            cursor.execute("SELECT ID, NOME FROM ALUNOS ORDER BY ID")
            data["alunos"] = [{"id": row[0], "nome": row[1]} for row in cursor.fetchall()]
            
        elif tipo_dados == "disciplinas":
            cursor.execute("SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID")
            data["disciplinas"] = [{"id": row[0], "nome": row[1]} for row in cursor.fetchall()]
            
        elif tipo_dados == "notas":
            cursor.execute("""
                SELECT n.ID, n.ID_ALUNO, a.NOME, n.ID_DISCIPLINA, d.NOME, n.NOTA 
                FROM NOTAS n 
                JOIN ALUNOS a ON n.ID_ALUNO = a.ID 
                JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID 
                ORDER BY n.ID
            """)
            data["notas"] = [
                {
                    "id": row[0],
                    "aluno": {"id": row[1], "nome": row[2]},
                    "disciplina": {"id": row[3], "nome": row[4]},
                    "nota": row[5]
                } for row in cursor.fetchall()
            ]
            
        elif tipo_dados == "todos":
            # Alunos
            cursor.execute("SELECT ID, NOME FROM ALUNOS ORDER BY ID")
            data["alunos"] = [{"id": row[0], "nome": row[1]} for row in cursor.fetchall()]
            
            # Disciplinas
            cursor.execute("SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID")
            data["disciplinas"] = [{"id": row[0], "nome": row[1]} for row in cursor.fetchall()]
            
            # Notas
            cursor.execute("""
                SELECT n.ID, n.ID_ALUNO, a.NOME, n.ID_DISCIPLINA, d.NOME, n.NOTA 
                FROM NOTAS n 
                JOIN ALUNOS a ON n.ID_ALUNO = a.ID 
                JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID 
                ORDER BY n.ID
            """)
            data["notas"] = [
                {
                    "id": row[0],
                    "aluno": {"id": row[1], "nome": row[2]},
                    "disciplina": {"id": row[3], "nome": row[4]},
                    "nota": row[5]
                } for row in cursor.fetchall()
            ]
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Arquivo '{filename}' criado com sucesso!")
        print("💡 Formato JSON estruturado para APIs e sistemas")
        
    except Exception as e:
        print(f"❌ Erro ao criar arquivo: {e}")
    
    input("Pressione Enter para continuar...")