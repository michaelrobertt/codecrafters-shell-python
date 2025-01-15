# 🐚 A Custom Shell Implementation that executes commands and manages processes using Python 🐍

[![progress-banner](https://backend.codecrafters.io/progress/shell/c05a9453-4908-4a80-8935-e9fd7048ae1e)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

This is a starting point for Python solutions to the
["Build Your Own Shell" Challenge](https://app.codecrafters.io/courses/shell/overview).

In this challenge, I did build my own POSIX compliant shell that's capable of
interpreting shell commands, running external programs and builtin commands like
cd, pwd, echo and more. Along the way, I learned about shell command parsing,
REPLs, builtin commands, and more.

**Note**: If you're viewing this repo on GitHub, head over to
[codecrafters.io](https://codecrafters.io) to try the challenge.

---

- [✨ Features](#-features)
  - [💡 Print a Prompt](#-print-a-prompt)
  - [🚫 Handle Invalid Commands](#-handle-invalid-commands)
  - [🔄 REPL (Read-Eval-Print Loop)](#-repl-read-eval-print-loop)
  - [📤 Built-in Commands](#-built-in-commands)
    - [🚪 Exit (`exit`)](#-exit-exit)
    - [🗣️ Echo (`echo`)](#️-echo-echo)
    - [🔍 Type (`type`)](#-type-type)
    - [📂 Change Directory (`cd`)](#-change-directory-cd)
    - [📍 Print Working Directory (`pwd`)](#-print-working-directory-pwd)
  - [🖋️ Quoting](#️-quoting)
  - [📜 Running External Programs](#-running-external-programs)

---

## 🛠️ Repository Setup

Para rodar este shell, basta clonar este repositório e executar o script `main.py`.

### Como rodar:

```bash
git clone <url-do-repositorio>
cd <diretorio-do-repositorio>
python main.py
```

## ✨ Features

### 💡 Print a Prompt

O shell exibe um prompt interativo (`$`) onde você pode digitar seus comandos.

### 🚫 Handle Invalid Commands

When an invalid command is entered, the shell gracefully notifies you instead of crashing:


### 🔄 REPL (Read-Eval-Print Loop)

The shell implements a REPL loop, continuously reading user input, evaluating it, and providing feedback. The loop only stops when you explicitly exit the shell.

### 📤 Built-in Commands

#### 🚪 Exit (exit)
Type exit 0 to exit the shell gracefully. 🛑

#### 🗣️ Echo (echo)
The echo command prints its arguments to the terminal. It also supports the -n flag to suppress the trailing newline.

#### 🔍 Type (type)
The type command checks if a command is a shell built-in or an external executable.

#### 📂 Change Directory (cd)
The cd command allows navigation of directories.

#### 📍 Print Working Directory (pwd)
The pwd command displays the current directory.

#### 🖋️ Quoting
Quoting mechanisms are fully supported to handle strings with spaces, special characters, and escape sequences.

#### 📜 Running External Programs
This shell allows running external commands by searching the system's $PATH for the executable.

---

## 🤝 Contributing

Contributions are welcome! 🎉 If you have ideas for new features or improvements, feel free to fork the repository, make changes, and submit a pull request. Please ensure all code is properly documented and tested.

💻 Happy coding and enjoy your new shell! 😊

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
