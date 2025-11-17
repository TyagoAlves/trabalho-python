from limpar_tela import limpar_tela

def inserir(cursor, conn, tipo):
    tipos = {
        "1": {"nome": "ALUNO", "tabela": "ALUNOS", "campo": "nome do aluno"},
        "2": {"nome": "DISCIPLINA", "tabela": "DISCIPLINAS", "campo": "nome da disciplina"}
    }
    
    config = tipos[tipo]
    
    limpar_tela()
    print("=" * 50)
    print(f"INSERINDO {config['nome']}".center(50))
    print("=" * 50)
    
    nome = input(f"Digite o {config['campo']}: ").strip()
    
    if not nome:
        print("Nome não pode estar vazio!")
        input("\nPressione Enter para continuar...")
        return False
    
    cursor.execute(f"INSERT INTO {config['tabela']} (NOME) VALUES (?)", (nome,))
    conn.commit()
    
    print(f"{config['nome']} inserido(a) com sucesso!")
    input("\nPressione Enter para continuar...")
    return True
