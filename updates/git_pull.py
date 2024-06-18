import os
import subprocess
import sys
import json
import datetime

with open("../paths/caminhos.json", "r") as jsonFile:
    data = json.load(jsonFile)

projetos = data['projetos']

with open("../logs/log_git_pull.log", "w") as log_file:
    log_file.write(datetime.date.today().strftime('%d/%m/%Y') + " - Start\n")

    # Rodar git pulls
    for projeto in projetos:
        print("Atualizando: " + projeto['nome'])
        log_file.write("---------- Projeto: " + projeto['nome'] + "----------\n")
        for index, servico in enumerate(projeto['servicos']):
            try:
                subprocess.check_output(["git", "checkout", servico['branch']], shell=True, stderr=subprocess.STDOUT, universal_newlines=True, cwd=servico['caminho'])
                saida_log = subprocess.check_output(["git", "pull", "origin", servico['branch']], shell=True, stderr=subprocess.STDOUT, universal_newlines=True, cwd=servico['caminho'])
                log_file.write(servico['nome'] + " - OK")
                print(servico['nome'] + " - OK (" + str(index + 1) + "/" + str(len(projeto['servicos'])) + ")")
                log_file.write("\n" + saida_log + "\n")
            except subprocess.CalledProcessError as e:
                print("\033[91m" + servico['nome'] + " - ERROR! (" + str(index + 1) + "/" + str(len(projeto['servicos'])) + ")" + "\033[0m")
                if "fatal: unable to access" in e.output:
                    print("\033[91m" + "Sem acesso ao repositório, verificar se você possui acesso a este projeto ou se está conectado na VPN!" + "\033[0m")
                if "Please commit your changes" in e.output:
                    print("\033[91m" + "Existem mudanças neste serviço que não foram comittadas!" + "\033[0m")
                log_file.write(servico['nome'] + " - ERROR")
                log_file.write("\n" + e.output)
        # gulp dist
        if "caminhoGulp" in projeto:
            try:
                print("Realizando gulp dist...")
                saida_log = subprocess.check_output(["gulp", "dist"], shell=True, stderr=subprocess.STDOUT, universal_newlines=True, cwd=projeto['caminhoGulp'])
                print("Gulp dist OK")
                log_file.write("**************************************** " + projeto['nome'] + " - Gulp OK ****************************************")
                log_file.write("\n" + saida_log + "\n")
                log_file.write("********************************************************************************\n")
            except subprocess.CalledProcessError as e:
                print("\033[91m" + projeto['nome'] + " - Gulp ERROR!" + "\033[0m")
                log_file.write("**************************************** " + projeto['nome'] + " - Gulp ERROR ****************************************")
                log_file.write("\n" + e.output)
                log_file.write("********************************************************************************\n")
        print("\n")


input("Projetos atualizados! Pressione Enter para fechar esta janela. ")
sys.exit()