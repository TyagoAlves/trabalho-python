import sqlite3
import time
from limpar_tela import limpar_tela
from inserir import inserir
from nota import inserir_nota, listar_notas, alterar_nota, excluir_nota
from listar import listar
from alterar import alterar
from excluir import excluir
from exportar import exportar_dados

def testar_conexao(conn: sqlite3.Connection) -> bool:
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        limpar_tela()
        print("Conectado ao banco com sucesso", end="")
        for _ in range(3):
            time.sleep(1)
            print(".", end="", flush=True)
        return True
    except sqlite3.Error:
        return False

def menu(cursor, conn):
    opcao = 1
    def exibir_submenu(acao):
        limpar_tela()
        print(f"""
Opções disponíveis para {acao}:
        1. Aluno
        2. Disciplina
        3. Nota
        4. Voltar
        """)
        sub_opcao = input("Digite uma opção: ")
        match sub_opcao:
            case "1":
                match acao.lower():
                    case "inserir":
                        try:
                            inserir(cursor, conn, sub_opcao)
                            print("Aluno inserido com sucesso!")
                        except Exception as e:
                            print(f"Erro ao inserir aluno: {e}")
                    case "listar":
                        listar(cursor, sub_opcao)
                    case "alterar":
                        alterar(cursor, conn, sub_opcao)
                    case "excluir":
                        excluir(cursor, conn, sub_opcao)

            case "2":
                match acao.lower():
                    case "inserir":
                        try:
                            inserir(cursor, conn, sub_opcao)
                            print("Disciplina inserida com sucesso!")
                        except Exception as e:
                            print(f"Erro ao inserir Disciplina: {e}")
                    case "listar":
                        listar(cursor, sub_opcao)
                    case "alterar":
                        alterar(cursor, conn, sub_opcao)
                    case "excluir":
                        excluir(cursor, conn, sub_opcao)

            case "3":
                match acao.lower():
                    case "inserir":
                        inserir_nota(cursor, conn)
                    case "listar":
                        listar_notas(cursor)
                    case "alterar":
                        alterar_nota(cursor, conn)
                    case "excluir":
                        excluir_nota(cursor, conn)       
            case _:
                print("Valor digitado invalido. Tente novamente!")

    def exibir_submenu_acao(sub_opcao):
        limpar_tela()
        print(f"""
Opções disponíveis para {sub_opcao}:
        1. ID
        2. Nome d{sub_opcao}
        """)
        return input("Digite uma opção: ")
    def exibir_submenu_aluno(acao, sub_opcao):
        limpar_tela()
        print(f"""
Opções disponíveis para {acao} {sub_opcao}:
        1. ID
        2. Nome do aluno
        """)
        return input("Digite uma opção: ")

    while opcao != "6":
        limpar_tela()
        print("=" * 50)
        print(f"SISTEMA ESCOLAR".center(50))
        print("=" * 50)
    
        print(
            """
Opções disponiveis:            
        1. Inserir 
        2. Alterar
        3. Listar
        4. Excluir
        5. Exportar Dados
        6. Sair
            """)
        opcao = input("Digite uma opção: ")
        match opcao:
            case "1":
                exibir_submenu("inserir")
            case "2":
                exibir_submenu("Alterar")
            case "3":
                exibir_submenu("Listar")
            case "4":
                exibir_submenu("Excluir")
            case "5":
                exportar_dados(cursor, conn)
            case "6":
                print("Você escolheu sair! ")                
            case _:
                print("Valor digitado invalido. Tente novamente!")
        



with sqlite3.connect('Banco.db') as conn:
    cursor = conn.cursor()
    testar_conexao(conn)

    sqlTabelaAlunos = """CREATE TABLE IF NOT EXISTS ALUNOS(
                        ID INTEGER NOT NULL,
                        NOME TEXT NOT NULL,
                        PRIMARY KEY (ID AUTOINCREMENT)
                    );"""
    sqlTabelaDisciplinas = """CREATE TABLE IF NOT EXISTS DISCIPLINAS(
                        ID INTEGER NOT NULL,
                        NOME TEXT NOT NULL,
                        PRIMARY KEY (ID AUTOINCREMENT)
                    );"""
    sqlTabelaNotas = """CREATE TABLE IF NOT EXISTS NOTAS(
                    ID INTEGER NOT NULL,
                    ID_ALUNO INTEGER NOT NULL,
                    ID_DISCIPLINA INTEGER NOT NULL,
                    NOTA REAL NOT NULL,
                    PRIMARY KEY (ID AUTOINCREMENT),
                    FOREIGN KEY (ID_ALUNO) REFERENCES ALUNOS(ID),
                    FOREIGN KEY (ID_DISCIPLINA) REFERENCES DISCIPLINAS(ID)
                );"""

    
    cursor.execute(sqlTabelaAlunos)
    cursor.execute(sqlTabelaDisciplinas)
    cursor.execute(sqlTabelaNotas)
    menu(cursor, conn)