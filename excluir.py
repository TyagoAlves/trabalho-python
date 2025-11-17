from limpar_tela import limpar_tela

def excluir(cursor, conn, tipo):
    
    tipos = {
        "1": {"nome": "ALUNO", "tabela": "ALUNOS"},
        "2": {"nome": "DISCIPLINA", "tabela": "DISCIPLINAS"}
    }
    
    limpar_tela()
    print("=" * 50)
    print(f"EXCLUINDO {tipos[tipo]['nome']}".center(50))
    print("=" * 50)
    

    cursor.execute(f"SELECT ID, NOME FROM {tipos[tipo]['tabela']} ORDER BY ID")
    dados = cursor.fetchall()
    
    if not dados:
        print(f"\nNenhum(a) {tipos[tipo]['nome'].lower()} cadastrado(a).")
        input("\nPressione Enter para continuar...")
        return False
    

    print(f"\n{'ID':<5} {'NOME':<30}")
    print("-" * 40)
    for item in dados:
        print(f"{item[0]:<5} {item[1]:<30}")
    

    try:
        id_excluir = int(input(f"\nDigite o ID d{('o' if tipo == '1' else 'a')} {tipos[tipo]['nome'].lower()} para excluir: "))
    except ValueError:
        print("ID inválido!")
        input("\nPressione Enter para continuar...")
        return False
    

    cursor.execute(f"SELECT NOME FROM {tipos[tipo]['tabela']} WHERE ID = ?", (id_excluir,))
    resultado = cursor.fetchone()
    
    if not resultado:
        print("ID não encontrado!")
        input("\nPressione Enter para continuar...")
        return False
    

    print(f"\nVocê tem certeza que deseja excluir:")
    print(f"ID: {id_excluir} - Nome: {resultado[0]}")
    confirmacao = input("Digite 'SIM' para confirmar: ").upper()
    
    if confirmacao != "SIM":
        print("Exclusão cancelada!")
        input("\nPressione Enter para continuar...")
        return False
    

    cursor.execute(f"DELETE FROM {tipos[tipo]['tabela']} WHERE ID = ?", (id_excluir,))
    conn.commit()
    
    print(f"{tipos[tipo]['nome']} excluído(a) com sucesso!")
    input("\nPressione Enter para continuar...")
    return True
