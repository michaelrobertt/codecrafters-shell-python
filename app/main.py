import sys
import os


# Função para encontrar um executável no PATH do sistema
def find_in_path(param):
    # Obtém o valor da variável de ambiente PATH, que contém os diretórios onde os executáveis estão localizados
    path = os.environ.get('PATH', '')
    
    # Itera sobre cada diretório no PATH
    for directory in path.split(os.pathsep):
        # Constrói o caminho completo para o executável
        possible_path = os.path.join(directory, param)
        
        # Verifica se o caminho é um arquivo executável
        if os.path.isfile(possible_path) and os.access(possible_path, os.X_OK):
            return possible_path  # Retorna o caminho se encontrar o executável
    
    return None  # Retorna None se o executável não for encontrado

# Função principal que simula um shell básico
def main():
    while True:
        # Exibe o prompt do shell
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        # Lê o comando digitado pelo usuário
        command = input().strip()
        
        # Usa pattern matching para tratar diferentes comandos
        match command.split(" "):
            # Caso o comando seja "exit 0", encerra o programa
            case ["exit", "0"]:
                exit(0)
            
            # Caso o comando seja "echo", imprime os argumentos seguintes
            case ["echo", *cmd]:
                print(" ".join(cmd))
            
            # Caso o comando seja "type", verifica se o comando é um builtin ou um executável no PATH
            case ["type", *cmd]:
                match cmd:
                    # Verifica se o comando é um builtin do shell
                    case ["echo" | "exit" | "type" | "pwd" | "cd"]:
                        print(f"{cmd[0]} is a shell builtin")
                    
                    # Caso contrário, tenta encontrar o executável no PATH
                    case _:
                        location = find_in_path(cmd[0])
                        if location:
                            print(f"{cmd[0]} is {location}")
                        else:
                            print(f"{' '.join(cmd)} not found")
                            
            case ["cd", *cmd]:
                if cmd[0] == '~':
                    os.chdir(os.getenv('HOME'))
                elif cmd:
                    try:
                        os.chdir(cmd[0])
                    except FileNotFoundError:
                        print(f"cd: {cmd[0]}: No such file or directory")
                            
            case ["pwd"]:
                print(f"{os.getcwd()}") #https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory
                #os.getcwd() (returns "a string representing the current working directory")
            
            # Caso o comando não seja reconhecido, tenta executá-lo como um comando externo
            case _:
                command_name = command.split()[0]
                if find_in_path(command_name):
                    os.system(command)  # Executa o comando no sistema
                else:
                    print(f"{command_name}: command not found")  # Mensagem de erro se o comando não for encontrado

# Ponto de entrada do programa
if __name__ == "__main__":
    main()