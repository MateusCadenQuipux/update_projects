import json
import autoit
import time

global janela_original


def map_debug(__config):
    return __config['debug_config']


def map_mvn(config):
    return config['mvn_update'] if 'mvn_update' in config else ''


def run_mvn(mvns, possiveis_mvn):
    old_index = 0

    autoit.send("!{F5}")
    autoit.win_wait_active("Update Maven Project")
    autoit.control_click("Update Maven Project", "Button3")
    autoit.control_click("Update Maven Project", "Button8")
    autoit.control_focus("Update Maven Project", "SysTreeView321")
    for mvn in mvns:
        index_atual = possiveis_mvn.index(mvn)
        tabs = index_atual - old_index
        autoit.send("{DOWN " + str(tabs) + "}")
        autoit.send('{SPACE}')
        old_index = index_atual
    autoit.control_click("Update Maven Project", "Button12")
    time.sleep(1)
    autoit.control_focus(janela_original, "Edit2")
    autoit.control_send(janela_original, "Edit2", "Progress")
    time.sleep(0.2)
    autoit.send("{ENTER}")
    texto_progresso = autoit.control_get_text(janela_original, "Static5")
    break_count = 0
    while texto_progresso != "Building workspace (Sleeping)":
        try:
            time.sleep(0.2)
            texto_progresso = autoit.control_get_text(janela_original, "Static5")
            break_count = 0
        except:
            break_count += 1
            if break_count == 10:
                break


def run_config(config_atual, fim):
    janela_debug = "Debug Configurations"

    autoit.send("!r")  # Digita ALT R
    autoit.send("b")  # Digita B
    autoit.win_wait_active(janela_debug)  # Espera a janela de debug config abrir
    autoit.control_focus(janela_debug, "Edit1")  # Foca no input de busca
    autoit.control_send(janela_debug, "Edit1", config_atual)  # Digita a config que rodará
    time.sleep(0.2)  # Espera a busca acontecer
    autoit.send("{ENTER}")  # Seleciona a config encontrada
    time.sleep(0.2)  # Espera para garantir que a config foi selecionada
    autoit.send("{ENTER}")  # Roda a config
    time.sleep(1)  # Espera 1s para não pegar o texto da run anterior

    texto_console = autoit.control_get_text(janela_original, "Static1")  # Pega o valor do texto acima do console
    while "terminated" not in texto_console and fim is False:  # Se o texto possuir "terminated", quebra o loop, caso contrário, espera e pega novamente
        time.sleep(0.5)
        texto_console = autoit.control_get_text(janela_original, "Static1")


with open("../paths/debug-config.json", "r") as jsonFile:
    data = json.load(jsonFile)

configs = data['configs']
possiveis_mvn = data['possiveis_mvn']
janela_original = data['nomeDaJanela']

autoit.opt("WinTitleMatchMode", 2) # Opção para só precisar buscar parte do nome da janela, ao invés do nome inteiro, que pode mudar
autoit.win_activate(janela_original)  # Abre a janela do STS
autoit.win_wait_active(janela_original)  # Espera abrir antes de continuar

# Rodando os maven update projects
mvns = list(map(map_mvn, configs))  # Pega uma lista com todos os mvns que rodarão
mvns = list(filter(None, mvns))  # Limpa valores vazios
mvns.sort()
run_mvn(mvns, possiveis_mvn)

# Rodando as debug configs
autoit.control_focus(janela_original, "Edit2")
autoit.control_send(janela_original, "Edit2", "Console")
time.sleep(0.2)
autoit.send("{ENTER}")
debug_configs = list(map(map_debug, configs))
for index, config in enumerate(debug_configs):  # Roda as configs
    isFim = index == len(configs) - 1
    run_config(config, isFim)
