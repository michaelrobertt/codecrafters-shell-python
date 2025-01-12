import sys

def main():
    
    valid_commands = ["exit 0"]  # Lista de comandos válidos
    while True:  # Mantém o loop para aceitar múltiplas entradas
        sys.stdout.write("$ ")
        sys.stdout.flush()  # Garante que o prompt seja exibido corretamente
        command = input()
        
        if command[:5] == 'echo ':
            word = command.replace("echo ", "")
            print(word)
        else:
            if command in valid_commands:
                if command == "exit 0":
                    break
            else:
                print(f"{command}: command not found")
    
if __name__ == "__main__":
    main()
