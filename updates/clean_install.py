import datetime
import json
import sys
import subprocess

def filtrar_projetos_back(projeto):
    if "caminhoGulp" not in projeto:
        return True
    else:
        return False

with open("../paths/caminhos.json", "r") as jsonFile:
    data = json.load(jsonFile)

projetos = filter(filtrar_projetos_back, data['projetos'])

with open("../logs/log_clean_install.log", "w") as log_file:
    log_file.write(datetime.date.today().strftime('%d/%m/%Y') + " - Start\n")

    for projeto in projetos:
        print("Atualizando: " + projeto['nome'])
        log_file.write("---------- Projeto: " + projeto['nome'] + "----------\n")
        for index, servico in enumerate(projeto['servicos']):
            try:
                saida_log = subprocess.check_output(["mvn", "clean", "install", "-DskipTests"], shell=True, stderr=subprocess.STDOUT, universal_newlines=True, cwd=servico['caminho'])
                log_file.write(servico['nome'] + " - OK")
                print(servico['nome'] + " - OK (" + str(index + 1) + "/" + str(len(projeto['servicos'])) + ")")
                log_file.write("\n" + saida_log + "\n")
            except subprocess.CalledProcessError as e:
                print("\033[91m" + servico['nome'] + " - ERROR! (" + str(index + 1) + "/" + str(len(projeto['servicos'])) + ")" + "\033[0m")
                log_file.write(servico['nome'] + " - ERROR")
                log_file.write("\n" + e.output)

input("JARs atualizados! Aperte ENTER para fechar esta janela.")

sys.exit()