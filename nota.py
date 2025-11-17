from limpar_tela import limpar_tela

def inserir_nota(cursor, conn):
    limpar_tela()
    print("=" * 50)
    print("INSERINDO NOTA".center(50))
    print("=" * 50)
    
    # Listar alunos
    cursor.execute("SELECT ID, NOME FROM ALUNOS ORDER BY ID")
    alunos = cursor.fetchall()
    
    if not alunos:
        print("Nenhum aluno cadastrado!")
        input("\nPressione Enter para continuar...")
        return False
    
    print("\nALUNOS DISPONÍVEIS:")
    print(f"{'ID':<5} {'NOME':<30}")
    print("-" * 40)
    for aluno in alunos:
        print(f"{aluno[0]:<5} {aluno[1]:<30}")
    
    # Selecionar aluno
    try:
        id_aluno = int(input("\nDigite o ID do aluno: "))
    except ValueError:
        print("ID inválido!")
        return False
    
    # Listar disciplinas
    cursor.execute("SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID")
    disciplinas = cursor.fetchall()
    
    if not disciplinas:
        print("Nenhuma disciplina cadastrada!")
        input("\nPressione Enter para continuar...")
        return False
    
    print("\nDISCIPLINAS DISPONÍVEIS:")
    print(f"{'ID':<5} {'NOME':<30}")
    print("-" * 40)
    for disciplina in disciplinas:
        print(f"{disciplina[0]:<5} {disciplina[1]:<30}")
    
    # Selecionar disciplina
    try:
        id_disciplina = int(input("\nDigite o ID da disciplina: "))
        nota = float(input("Digite a nota (0-10): "))
    except ValueError:
        print("Valores inválidos!")
        return False
    
    # Validar nota
    if not (0 <= nota <= 10):
        print("Nota deve estar entre 0 e 10!")
        return False
    
    # Inserir nota
    cursor.execute("INSERT INTO NOTAS (ID_ALUNO, ID_DISCIPLINA, NOTA) VALUES (?, ?, ?)", 
                   (id_aluno, id_disciplina, nota))
    conn.commit()
    
    print("Nota inserida com sucesso!")
    input("\nPressione Enter para continuar...")
    return True

def listar_notas(cursor):
    limpar_tela()
    print("=" * 50)
    print("LISTA DE NOTAS".center(50))
    print("=" * 50)
    
    print("\nOpções de listagem:")
    print("1. Todas as notas")
    print("2. Notas por aluno")
    print("3. Notas por disciplina")
    
    try:
        opcao = input("\nEscolha uma opção (1-3): ")
    except:
        opcao = "1"
    
    if opcao == "2":
        listar_notas_por_aluno(cursor)
    elif opcao == "3":
        listar_notas_por_disciplina(cursor)
    else:
        listar_todas_notas(cursor)
    
    return True

def listar_todas_notas(cursor):
    """Lista todas as notas"""
    cursor.execute("""
        SELECT n.ID, a.NOME, d.NOME, n.NOTA 
        FROM NOTAS n
        JOIN ALUNOS a ON n.ID_ALUNO = a.ID
        JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID
        ORDER BY a.NOME, d.NOME
    """)
    notas = cursor.fetchall()
    
    if not notas:
        print("\nNenhuma nota cadastrada.")
    else:
        print(f"\n{'ID':<5} {'ALUNO':<20} {'DISCIPLINA':<20} {'NOTA':<5}")
        print("-" * 55)
        for nota in notas:
            print(f"{nota[0]:<5} {nota[1]:<20} {nota[2]:<20} {nota[3]:<5}")
    
    input("\nPressione Enter para continuar...")

def listar_notas_por_aluno(cursor):
    """Lista notas filtradas por aluno"""
    print("\n" + "=" * 30)
    print("FILTRAR POR ALUNO")
    print("=" * 30)
    
    busca = input("Digite o ID ou nome do aluno: ").strip()
    if not busca:
        print("Busca cancelada.")
        input("\nPressione Enter para continuar...")
        return
    
    try:
        if busca.isdigit():
            # Busca por ID
            cursor.execute("""
                SELECT n.ID, a.NOME, d.NOME, n.NOTA 
                FROM NOTAS n
                JOIN ALUNOS a ON n.ID_ALUNO = a.ID
                JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID
                WHERE a.ID = ?
                ORDER BY d.NOME
            """, (int(busca),))
        else:
            # Busca por nome
            cursor.execute("""
                SELECT n.ID, a.NOME, d.NOME, n.NOTA 
                FROM NOTAS n
                JOIN ALUNOS a ON n.ID_ALUNO = a.ID
                JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID
                WHERE a.NOME LIKE ?
                ORDER BY d.NOME
            """, (f"%{busca}%",))
        
        notas = cursor.fetchall()
        
        if not notas:
            print(f"\nNenhuma nota encontrada para '{busca}'.")
        else:
            print(f"\nNotas encontradas para '{busca}':")
            print(f"\n{'ID':<5} {'ALUNO':<20} {'DISCIPLINA':<20} {'NOTA':<5}")
            print("-" * 55)
            for nota in notas:
                print(f"{nota[0]:<5} {nota[1]:<20} {nota[2]:<20} {nota[3]:<5}")
    
    except Exception as e:
        print(f"Erro ao buscar: {e}")
    
    input("\nPressione Enter para continuar...")

def listar_notas_por_disciplina(cursor):
    """Lista notas filtradas por disciplina"""
    print("\n" + "=" * 30)
    print("FILTRAR POR DISCIPLINA")
    print("=" * 30)
    
    busca = input("Digite o ID ou nome da disciplina: ").strip()
    if not busca:
        print("Busca cancelada.")
        input("\nPressione Enter para continuar...")
        return
    
    try:
        if busca.isdigit():
            # Busca por ID
            cursor.execute("""
                SELECT n.ID, a.NOME, d.NOME, n.NOTA 
                FROM NOTAS n
                JOIN ALUNOS a ON n.ID_ALUNO = a.ID
                JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID
                WHERE d.ID = ?
                ORDER BY a.NOME
            """, (int(busca),))
        else:
            # Busca por nome
            cursor.execute("""
                SELECT n.ID, a.NOME, d.NOME, n.NOTA 
                FROM NOTAS n
                JOIN ALUNOS a ON n.ID_ALUNO = a.ID
                JOIN DISCIPLINAS d ON n.ID_DISCIPLINA = d.ID
                WHERE d.NOME LIKE ?
                ORDER BY a.NOME
            """, (f"%{busca}%",))
        
        notas = cursor.fetchall()
        
        if not notas:
            print(f"\nNenhuma nota encontrada para '{busca}'.")
        else:
            print(f"\nNotas encontradas para '{busca}':")
            print(f"\n{'ID':<5} {'ALUNO':<20} {'DISCIPLINA':<20} {'NOTA':<5}")
            print("-" * 55)
            for nota in notas:
                print(f"{nota[0]:<5} {nota[1]:<20} {nota[2]:<20} {nota[3]:<5}")
    
    except Exception as e:
        print(f"Erro ao buscar: {e}")
    
    input("\nPressione Enter para continuar...")
def alterar_nota(cursor, conn):
    limpar_tela()
    print("=" * 50)
    print("ALTERANDO NOTA".center(50))
    print("=" * 50)
    
    # Listar alunos disponíveis
    cursor.execute("SELECT ID, NOME FROM ALUNOS ORDER BY ID")
    alunos = cursor.fetchall()
    
    if not alunos:
        print("Nenhum aluno cadastrado!")
        input("\nPressione Enter para continuar...")
        return False
    
    print("\nALUNOS DISPONÍVEIS:")
    print(f"{'ID':<5} {'NOME':<30}")
    print("-" * 40)
    for aluno in alunos:
        print(f"{aluno[0]:<5} {aluno[1]:<30}")
    
    # Selecionar aluno
    try:
        id_aluno = int(input("\nDigite o ID do aluno: "))
    except ValueError:
        print("ID inválido!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Verificar se aluno existe
    cursor.execute("SELECT NOME FROM ALUNOS WHERE ID = ?", (id_aluno,))
    aluno_nome = cursor.fetchone()
    if not aluno_nome:
        print("Aluno não encontrado!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Listar disciplinas disponíveis
    cursor.execute("SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID")
    disciplinas = cursor.fetchall()
    
    if not disciplinas:
        print("Nenhuma disciplina cadastrada!")
        input("\nPressione Enter para continuar...")
        return False
    
    print(f"\nDISCIPLINAS DISPONÍVEIS PARA {aluno_nome[0]}:")
    print(f"{'ID':<5} {'NOME':<30}")
    print("-" * 40)
    for disciplina in disciplinas:
        print(f"{disciplina[0]:<5} {disciplina[1]:<30}")
    
    # Selecionar disciplina
    try:
        id_disciplina = int(input("\nDigite o ID da disciplina: "))
    except ValueError:
        print("ID inválido!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Verificar se disciplina existe
    cursor.execute("SELECT NOME FROM DISCIPLINAS WHERE ID = ?", (id_disciplina,))
    disciplina_nome = cursor.fetchone()
    if not disciplina_nome:
        print("Disciplina não encontrada!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Verificar se existe nota para essa combinação aluno/disciplina
    cursor.execute("""
        SELECT ID, NOTA FROM NOTAS 
        WHERE ID_ALUNO = ? AND ID_DISCIPLINA = ?
    """, (id_aluno, id_disciplina))
    nota_existente = cursor.fetchone()
    
    if not nota_existente:
        print(f"\nNenhuma nota encontrada para:")
        print(f"Aluno: {aluno_nome[0]}")
        print(f"Disciplina: {disciplina_nome[0]}")
        input("\nPressione Enter para continuar...")
        return False
    
    # Mostrar dados atuais e solicitar nova nota
    print(f"\nAluno: {aluno_nome[0]}")
    print(f"Disciplina: {disciplina_nome[0]}")
    print(f"Nota atual: {nota_existente[1]}")
    
    try:
        nova_nota = float(input("Digite a nova nota (0-10): "))
    except ValueError:
        print("Nota inválida!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Validar nota
    if not (0 <= nova_nota <= 10):
        print("Nota deve estar entre 0 e 10!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Atualizar no banco
    cursor.execute("""
        UPDATE NOTAS SET NOTA = ? 
        WHERE ID_ALUNO = ? AND ID_DISCIPLINA = ?
    """, (nova_nota, id_aluno, id_disciplina))
    conn.commit()
    
    print("Nota alterada com sucesso!")
    input("\nPressione Enter para continuar...")
    return True


def excluir_nota(cursor, conn):
    limpar_tela()
    print("=" * 50)
    print("EXCLUINDO NOTA".center(50))
    print("=" * 50)
    
    # Listar alunos disponíveis
    cursor.execute("SELECT ID, NOME FROM ALUNOS ORDER BY ID")
    alunos = cursor.fetchall()
    
    if not alunos:
        print("Nenhum aluno cadastrado!")
        input("\nPressione Enter para continuar...")
        return False
    
    print("\nALUNOS DISPONÍVEIS:")
    print(f"{'ID':<5} {'NOME':<30}")
    print("-" * 40)
    for aluno in alunos:
        print(f"{aluno[0]:<5} {aluno[1]:<30}")
    
    # Selecionar aluno
    try:
        id_aluno = int(input("\nDigite o ID do aluno: "))
    except ValueError:
        print("ID inválido!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Verificar se aluno existe
    cursor.execute("SELECT NOME FROM ALUNOS WHERE ID = ?", (id_aluno,))
    aluno_nome = cursor.fetchone()
    if not aluno_nome:
        print("Aluno não encontrado!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Listar disciplinas disponíveis
    cursor.execute("SELECT ID, NOME FROM DISCIPLINAS ORDER BY ID")
    disciplinas = cursor.fetchall()
    
    if not disciplinas:
        print("Nenhuma disciplina cadastrada!")
        input("\nPressione Enter para continuar...")
        return False
    
    print(f"\nDISCIPLINAS DISPONÍVEIS PARA {aluno_nome[0]}:")
    print(f"{'ID':<5} {'NOME':<30}")
    print("-" * 40)
    for disciplina in disciplinas:
        print(f"{disciplina[0]:<5} {disciplina[1]:<30}")
    
    # Selecionar disciplina
    try:
        id_disciplina = int(input("\nDigite o ID da disciplina: "))
    except ValueError:
        print("ID inválido!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Verificar se disciplina existe
    cursor.execute("SELECT NOME FROM DISCIPLINAS WHERE ID = ?", (id_disciplina,))
    disciplina_nome = cursor.fetchone()
    if not disciplina_nome:
        print("Disciplina não encontrada!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Verificar se existe nota para essa combinação aluno/disciplina
    cursor.execute("""
        SELECT ID, NOTA FROM NOTAS 
        WHERE ID_ALUNO = ? AND ID_DISCIPLINA = ?
    """, (id_aluno, id_disciplina))
    nota_existente = cursor.fetchone()
    
    if not nota_existente:
        print(f"\nNenhuma nota encontrada para:")
        print(f"Aluno: {aluno_nome[0]}")
        print(f"Disciplina: {disciplina_nome[0]}")
        input("\nPressione Enter para continuar...")
        return False
    
    # Confirmar exclusão
    print(f"\nVocê tem certeza que deseja excluir:")
    print(f"Aluno: {aluno_nome[0]}")
    print(f"Disciplina: {disciplina_nome[0]}")
    print(f"Nota: {nota_existente[1]}")
    confirmacao = input("Digite 'SIM' para confirmar: ").upper()
    
    if confirmacao != "SIM":
        print("Exclusão cancelada!")
        input("\nPressione Enter para continuar...")
        return False
    
    # Excluir do banco
    cursor.execute("""
        DELETE FROM NOTAS 
        WHERE ID_ALUNO = ? AND ID_DISCIPLINA = ?
    """, (id_aluno, id_disciplina))
    conn.commit()
    
    print("Nota excluída com sucesso!")
    input("\nPressione Enter para continuar...")
    return True

