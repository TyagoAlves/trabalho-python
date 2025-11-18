
import sqlite3
from exportar import exportar_txt, exportar_csv, exportar_json


with sqlite3.connect('exemplo.db') as conn:
    cursor = conn.cursor()
    

    cursor.execute("""CREATE TABLE IF NOT EXISTS ALUNOS(
                        ID INTEGER NOT NULL,
                        NOME TEXT NOT NULL,
                        PRIMARY KEY (ID AUTOINCREMENT)
                    );""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS DISCIPLINAS(
                        ID INTEGER NOT NULL,
                        NOME TEXT NOT NULL,
                        PRIMARY KEY (ID AUTOINCREMENT)
                    );""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS NOTAS(
                    ID INTEGER NOT NULL,
                    ID_ALUNO INTEGER NOT NULL,
                    ID_DISCIPLINA INTEGER NOT NULL,
                    NOTA REAL NOT NULL,
                    PRIMARY KEY (ID AUTOINCREMENT),
                    FOREIGN KEY (ID_ALUNO) REFERENCES ALUNOS(ID),
                    FOREIGN KEY (ID_DISCIPLINA) REFERENCES DISCIPLINAS(ID)
                );""")
    

    cursor.execute("INSERT INTO ALUNOS (NOME) VALUES ('João Silva')")
    cursor.execute("INSERT INTO ALUNOS (NOME) VALUES ('Maria Santos')")
    cursor.execute("INSERT INTO ALUNOS (NOME) VALUES ('Pedro Costa')")
    
    cursor.execute("INSERT INTO DISCIPLINAS (NOME) VALUES ('Matemática')")
    cursor.execute("INSERT INTO DISCIPLINAS (NOME) VALUES ('Português')")
    cursor.execute("INSERT INTO DISCIPLINAS (NOME) VALUES ('História')")
    
    cursor.execute("INSERT INTO NOTAS (ID_ALUNO, ID_DISCIPLINA, NOTA) VALUES (1, 1, 8.5)")
    cursor.execute("INSERT INTO NOTAS (ID_ALUNO, ID_DISCIPLINA, NOTA) VALUES (1, 2, 9.0)")
    cursor.execute("INSERT INTO NOTAS (ID_ALUNO, ID_DISCIPLINA, NOTA) VALUES (2, 1, 7.5)")
    cursor.execute("INSERT INTO NOTAS (ID_ALUNO, ID_DISCIPLINA, NOTA) VALUES (2, 3, 8.0)")
    
    conn.commit()
    
    print(" Banco de exemplo criado!")
    print(" Gerando arquivos de exemplo...")
    

    exportar_txt("alunos", cursor)
    exportar_csv("disciplinas", cursor) 
    exportar_json("notas", cursor)
    
    print(" Exemplos de exportação criados com sucesso!")
