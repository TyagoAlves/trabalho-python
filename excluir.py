from limpar_tela import limpar_tela

def excluir(cursor, conn, tipo):
    # Mapeamento dos tipos
    tipos = {
        "1": {"nome": "ALUNO", "tabela": "ALUNOS"},
        "2": {"nome": "DISCIPLINA", "tabela": "DISCIPLINAS"}
    }
    
    limpar_tela()
    print("=" * 50)
    print(f"EXCLUINDO {tipos[tipo]['nome']}".center(50))
    print("=" * 50)
    
    # Listar registros existentes
    cursor.execute(f"SELECT ID, NOME FROM {tipos[tipo]['tabela']} ORDER BY ID")
    dados = cursor.fetchall()
    
    if not dados:
        print(f"\nNenhum(a) {tipos[tipo]['nome'].lower()} cadastrado(a).")
        input("\nPressione Enter para continuar...")
        return False
    
    # Mostrar lista
    print(f"\n{'ID':<5} {'NOME':<30}")
    print("-" * 40)
    for item in dados:
        print(f"{item[0]:<5} {item[1]:<30}")
    
    # Solicitar ID para excluir
    try:
        id_excluir = int(input(f"\nDigite o ID d{('o' if tipo == '1' else 'a')} {tipos[tipo]['nome'].lower()} para excluir: "))
    except ValueError:
        print("ID inválido!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Verificar se ID existe
    cursor.execute(f"SELECT NOME FROM {tipos[tipo]['tabela']} WHERE ID = ?", (id_excluir,))
    resultado = cursor.fetchone()
    
    if not resultado:
        print("ID não encontrado!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Confirmar exclusão
    print(f"\nVocê tem certeza que deseja excluir:")
    print(f"ID: {id_excluir} - Nome: {resultado[0]}")
    confirmacao = input("Digite 'SIM' para confirmar: ").upper()
    
    if confirmacao != "SIM":
        print("Exclusão cancelada!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Excluir do banco
    cursor.execute(f"DELETE FROM {tipos[tipo]['tabela']} WHERE ID = ?", (id_excluir,))
    conn.commit()
    
    print(f"{tipos[tipo]['nome']} excluído(a) com sucesso!")
    input("\nPressione Enter para continuar...")
    return True
