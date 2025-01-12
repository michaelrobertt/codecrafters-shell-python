import sys

def main():
    valid_commands = ["mkdir", "exit"]  # Lista de comandos válidos
    while True:  # Mantém o loop para aceitar múltiplas entradas
        sys.stdout.write("$ ")
        sys.stdout.flush()  # Garante que o prompt seja exibido corretamente
        command = input()
        
        if command in valid_commands:
            if command == "mkdir":
                print("mkdir: comando executado (simulação)")  # Exemplo de execução
            elif command == "exit":
                print("Saindo...")
                break  # Encerra o loop
        else:
            print(f"{command}: command not found")
    
if __name__ == "__main__":
    main()
