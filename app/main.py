import sys
import shutil

def main():
    valid_commands = ["cat", "cp", "mkdir", "my_exe"]  # Lista de comandos válidos
    shell_builtin = ["exit 0", "exit", "echo", "type", ]  # Lista de comandos internos
    
    while True:  # Mantém o loop para aceitar múltiplas entradas
        sys.stdout.write("$ ")
        sys.stdout.flush()  # Garante que o prompt seja exibido corretamente
        
        input_command = input().strip()  # Remove espaços vazios no início e no fim
        
        parted_command = input_command.split()  # Divide a string por espaços
        if not parted_command:  # Ignora entrada vazia
            continue
        
        cmd = parted_command[0]
        args = parted_command[1:]  # Lista com todos os argumentos
        
        if cmd == "echo":
            print(" ".join(args))  # Imprime todos os argumentos como uma string
        elif cmd == "type":
            if args and args[0] in valid_commands: # Verifica se args não está vazio e dps acessa o args 0     
                path = shutil.which(args[0])  # Retorna o caminho do executável do comando https://docs.python.org/3/library/shutil.html
                print(f"{args[0]} is {path}")
            elif args and args[0] in shell_builtin:
                print(f"{args[0]} is a shell builtin")
            else:
                print(f"{args[0]}: not found")
        elif cmd == "exit" or cmd == "exit 0" and not args:
                break
        else:
            print(f"{cmd}: not found")

if __name__ == "__main__":
    main()