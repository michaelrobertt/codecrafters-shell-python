import sys
import os
import shlex
import subprocess

# Função que procura um executável no PATH do sistema
def find_in_path(param):
    # Obtém o valor da variável de ambiente PATH
    path = os.environ.get('PATH', '')
    # Itera sobre cada diretório no PATH
    for directory in path.split(os.pathsep):
        # Cria o caminho completo do possível executável
        possible_path = os.path.join(directory, param)
        # Verifica se o caminho é um arquivo executável
        if os.path.isfile(possible_path) and os.access(possible_path, os.X_OK):
            return possible_path
    return None

# Função que processa um comando, juntando os argumentos com um espaço
def processar_comando(cmd):
    # Junta os argumentos com um espaço, preservando os espaços dentro de aspas
    return ' '.join(cmd)

# Função principal que implementa o loop do shell
def main():
    while True:
        # Exibe o prompt do shell
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Lê o comando do usuário
        command = input().strip()
        
        # Analisa o comando usando shlex.split para lidar com aspas e espaços
        tokens = shlex.split(command, posix=True)
        
        # Se não houver tokens, continua para o próximo loop (ignora linhas em branco)
        if not tokens:
            continue
        
        # Estrutura de correspondência para tratar diferentes comandos
        match tokens:
            # Caso o comando seja "exit 0", encerra o shell
            case ["exit", "0"]:
                exit(0)
            
            # Caso o comando seja "echo"
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
            
            # Caso o comando seja "type"
            case ["type", *cmd]:
                # Verifica se o comando é um builtin do shell
                if cmd[0] in ["echo", "exit", "type", "pwd", "cd"]:
                    print(f"{cmd[0]} is a shell builtin")
                else:
                    # Procura o comando no PATH
                    location = find_in_path(cmd[0])
                    if location:
                        print(f"{cmd[0]} is {location}")
                    else:
                        print(f"{' '.join(cmd)} not found")
            
            # Caso o comando seja "cd"
            case ["cd", *cmd]:
                if cmd:
                    target = cmd[0]
                    # Se o destino for ~, muda para o diretório HOME
                    if target == '~':
                        target = os.getenv('HOME')
                    try:
                        os.chdir(target)
                    except FileNotFoundError:
                        print(f"cd: {target}: No such file or directory")
                else:
                    # Se não houver argumento, muda para o diretório HOME
                    os.chdir(os.getenv('HOME'))
            
            # Caso o comando seja "pwd"
            case ["pwd"]:
                # Imprime o diretório atual
                print(os.getcwd())
            
            # Caso o comando não corresponda a nenhum dos anteriores
            case _:
                command_name = tokens[0]
                args = tokens[1:]
                # Procura o comando no PATH
                location = find_in_path(command_name)
                if location:
                    try:
                        # Obtém apenas o nome do programa sem o caminho
                        prog_name = os.path.basename(location)
                        # Executa o comando com subprocess.run
                        result = subprocess.run([prog_name] + args, capture_output=True, text=True)
                        # Imprime a saída padrão do comando
                        print(result.stdout, end='')
                        # Imprime a saída de erro, se houver
                        if result.stderr:
                            print(result.stderr, file=sys.stderr, end='')
                    except Exception as e:
                        print(f"Error executing {command_name}: {e}", file=sys.stderr)
                else:
                    print(f"{command_name}: command not found")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()