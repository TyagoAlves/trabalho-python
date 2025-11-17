from limpar_tela import limpar_tela

def listar(cursor, tipo):
    tipos = {"1": "ALUNOS", "2": "DISCIPLINAS"}
    
    limpar_tela()
    print("=" * 50)
    print(f"LISTA DE {tipos[tipo]}".center(50))
    print("=" * 50)
    
    cursor.execute(f"SELECT ID, NOME FROM {tipos[tipo]} ORDER BY ID")
    dados = cursor.fetchall()
    
    if not dados:
        print(f"\nNenhum(a) {tipos[tipo].lower()} cadastrado(a).")
    else:
        print(f"\n{'ID':<5} {'NOME':<30}")
        print("-" * 40)
        for item in dados:
            print(f"{item[0]:<5} {item[1]:<30}")
    
    input("\nPressione Enter para continuar...")
    return True