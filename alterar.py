from limpar_tela import limpar_tela

def alterar(cursor, conn, tipo):
    # Mapeamento dos tipos
    tipos = {
        "1": {"nome": "ALUNO", "tabela": "ALUNOS", "campo": "nome do aluno"},
        "2": {"nome": "DISCIPLINA", "tabela": "DISCIPLINAS", "campo": "nome da disciplina"}
    }
    
    limpar_tela()
    print("=" * 50)
    print(f"ALTERANDO {tipos[tipo]['nome']}".center(50))
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
    
    # Solicitar ID para alterar
    try:
        id_alterar = int(input(f"\nDigite o ID d{('o' if tipo == '1' else 'a')} {tipos[tipo]['nome'].lower()} para alterar: "))
    except ValueError:
        print("ID inválido!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Verificar se ID existe
    cursor.execute(f"SELECT NOME FROM {tipos[tipo]['tabela']} WHERE ID = ?", (id_alterar,))
    resultado = cursor.fetchone()
    
    if not resultado:
        print("ID não encontrado!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Mostrar dados atuais e solicitar novo nome
    print(f"\nNome atual: {resultado[0]}")
    novo_nome = input(f"Digite o novo {tipos[tipo]['campo']}: ").strip()
    
    if not novo_nome:
        print("Nome não pode estar vazio!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Atualizar no banco
    cursor.execute(f"UPDATE {tipos[tipo]['tabela']} SET NOME = ? WHERE ID = ?", (novo_nome, id_alterar))
    conn.commit()
    
    print(f"{tipos[tipo]['nome']} alterado(a) com sucesso!")
    input("\nPressione Enter para continuar...")
    return True
