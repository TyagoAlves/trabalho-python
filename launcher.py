import sys
import os

def escolher_interface():
    print("=" * 50)
    print("SISTEMA ESCOLAR - LAUNCHER".center(50))
    print("=" * 50)
    print("\nEscolha como deseja executar o sistema:")
    print("1. Terminal (Interface de texto)")
    print("2. Interface Gráfica (Tkinter)")
    print("3. Sair")
    
    while True:
        opcao = input("\nDigite sua opção (1-3): ")
        
        match opcao:
            case "1":
                print("\nIniciando sistema no terminal...")
                import main  # Executa o sistema atual
                break
            case "2":
                print("\nIniciando interface gráfica...")
                try:
                    import gui_main
                    gui_main.main()  # ✅ Executa a GUI
                except ImportError:
                    print("Interface gráfica não disponível!")
                    print("Execute: pip install tkinter")
                except Exception as e:
                    print(f"Erro ao iniciar interface gráfica: {e}")
                break
            case "3":
                print("Saindo...")
                sys.exit()
            case _:
                print("Opção inválida! Digite 1, 2 ou 3.")

if __name__ == "__main__":
    escolher_interface()
