import os
import subprocess

class Limpeza:
    def __init__(self):
        pass


    def limpar_terminal(self):
        
        #checa o sistema operacional e limpa o terminal
        if os.name == 'nt':
            subprocess.run('cls', shell=True, check=False)
        else:
            subprocess.run(['clear'], check=False)
