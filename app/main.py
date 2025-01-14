import sys
import os
import shlex
import subprocess

def find_in_path(param):
    # Obtém o valor da variável de ambiente PATH
    path = os.environ.get('PATH', '')
    for directory in path.split(os.pathsep):
        possible_path = os.path.join(directory, param)
        if os.path.isfile(possible_path) and os.access(possible_path, os.X_OK):
            return possible_path
    return None

def processar_comando(cmd):
    # Junta os argumentos com um espaço, preservando os espaços dentro de aspas
    return ' '.join(cmd)

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()
        
        # Analisa o comando usando shlex.split para lidar com aspas e espaços
        tokens = shlex.split(command, posix=True)
        
        if not tokens:
            continue  # Ignora linhas em branco
        
        match tokens:
            case ["exit", "0"]:
                exit(0)
            
            case ["echo", *cmd]:
                # Verifica se a opção -n está presente
                if cmd and cmd[0] == '-n':
                    # Remove -n e imprime sem nova linha
                    cmd = cmd[1:]
                    resultado = processar_comando(cmd)
                    print(resultado, end='')
                else:
                    # Imprime com nova linha
                    resultado = processar_comando(cmd)
                    print(resultado)
            
            case ["type", *cmd]:
                if cmd[0] in ["echo", "exit", "type", "pwd", "cd"]:
                    print(f"{cmd[0]} is a shell builtin")
                else:
                    location = find_in_path(cmd[0])
                    if location:
                        print(f"{cmd[0]} is {location}")
                    else:
                        print(f"{' '.join(cmd)} not found")
            
            case ["cd", *cmd]:
                if cmd:
                    target = cmd[0]
                    if target == '~':
                        target = os.getenv('HOME')
                    try:
                        os.chdir(target)
                    except FileNotFoundError:
                        print(f"cd: {target}: No such file or directory")
                else:
                    os.chdir(os.getenv('HOME'))
            
            case ["pwd"]:
                print(os.getcwd())
            
            case _:
                command_name = tokens[0]
                args = tokens[1:]
                location = find_in_path(command_name)
                if location:
                    try:
                        # Obtém apenas o nome do programa sem o caminho
                        prog_name = os.path.basename(location)
                        # Executa o comando com subprocess.run
                        result = subprocess.run([prog_name] + args, capture_output=True, text=True)
                        print(result.stdout, end='')
                        if result.stderr:
                            print(result.stderr, file=sys.stderr, end='')
                    except Exception as e:
                        print(f"Error executing {command_name}: {e}", file=sys.stderr)
                else:
                    print(f"{command_name}: command not found")

if __name__ == "__main__":
    main()