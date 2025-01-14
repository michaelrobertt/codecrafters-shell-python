import sys
import os
import shlex
import subprocess

# Função que verifica se um comando existe no sistema pesquisando no PATH
def find_in_path(param):
    # A variável PATH armazena os diretórios onde os executáveis estão localizados
    path = os.environ.get('PATH', '')
    for directory in path.split(os.pathsep):  # Divide o PATH em uma lista de diretórios
        possible_path = os.path.join(directory, param)  # Cria um caminho completo para o comando
        # Verifica se o caminho é um arquivo e se é executável
        if os.path.isfile(possible_path) and os.access(possible_path, os.X_OK):
            return possible_path  # Retorna o caminho completo se for encontrado
    return None  # Retorna None se o comando não for encontrado

# Função para juntar argumentos em uma string de comando

def processar_comando(cmd):
    # Junta os argumentos mantendo espaços em torno de palavras com aspas
    return ' '.join(cmd)

# Função principal que atua como um simulador de shell

def main():
    while True:
        sys.stdout.write("$ ")  # Imprime o prompt do shell
        sys.stdout.flush()  # Garante que o prompt seja exibido imediatamente
        command = input().strip()  # Lê o comando do usuário e remove espaços extras

        # Divide o comando usando shlex.split para tratar espaços e aspas corretamente
        tokens = shlex.split(command, posix=True)

        if not tokens:
            continue  # Ignora entradas em branco

        match tokens:
            case ["exit", "0"]:
                exit(0)  # Sai do programa quando o usuário digita "exit 0"

            case ["echo", *cmd]:
                # Se o primeiro argumento for "-n", remove-o e imprime sem nova linha
                if cmd and cmd[0] == '-n':
                    cmd = cmd[1:]
                    resultado = processar_comando(cmd)
                    print(resultado, end='')
                else:
                    resultado = processar_comando(cmd)
                    print(resultado)

            case ["type", *cmd]:
                # Verifica se o comando é um comando interno da shell
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
                        target = os.getenv('HOME')  # Substitui "~" pelo diretório home do usuário
                    try:
                        os.chdir(target)  # Tenta mudar para o diretório especificado
                    except FileNotFoundError:
                        print(f"cd: {target}: No such file or directory")
                else:
                    os.chdir(os.getenv('HOME'))  # Se "cd" for usado sem argumento, vai para o diretório home

            case ["pwd"]:
                print(os.getcwd())  # Exibe o diretório atual

            case _:
                command_name = tokens[0]  # Primeiro token é o nome do comando
                args = tokens[1:]  # Os demais são os argumentos
                location = find_in_path(command_name)
                if location:
                    try:
                        # Executa o comando usando subprocess.run e captura a saída
                        result = subprocess.run([location] + args, capture_output=True, text=True)
                        print(result.stdout, end='')
                        if result.stderr:
                            print(result.stderr, file=sys.stderr, end='')
                    except Exception as e:
                        print(f"Error executing {command_name}: {e}", file=sys.stderr)
                else:
                    print(f"{command_name}: command not found")

if __name__ == "__main__":
    main()
