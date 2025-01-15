# michaelrobertt-codecrafters-shell-python
A shell command-line interface that executes commands and manages processes.
=======
[![progress-banner](https://backend.codecrafters.io/progress/shell/c05a9453-4908-4a80-8935-e9fd7048ae1e)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

This is a starting point for Python solutions to the
["Build Your Own Shell" Challenge](https://app.codecrafters.io/courses/shell/overview).

In this challenge, I did build my own POSIX compliant shell that's capable of
interpreting shell commands, running external programs and builtin commands like
cd, pwd, echo and more. Along the way, I learned about shell command parsing,
REPLs, builtin commands, and more.

**Note**: If you're viewing this repo on GitHub, head over to
[codecrafters.io](https://codecrafters.io) to try the challenge.

# 🐚 Custom Shell Implementation using Python 🐍

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
    - [Single Quotes](#single-quotes)
    - [Double Quotes](#double-quotes)
    - [Backslash Outside Quotes](#backslash-outside-quotes)
    - [Backslash Within Single Quotes](#backslash-within-single-quotes)
    - [Backslash Within Double Quotes](#backslash-within-double-quotes)
    - [Executing a Quoted Command](#executing-a-quoted-command)
      
  - [📜 Running External Programs](#-running-external-programs)
    
- [📂 Directory Structure](#-directory-structure)

---
