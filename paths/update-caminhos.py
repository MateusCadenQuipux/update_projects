import json

with open("caminhos.json", "r") as jsonFile:
    data = json.load(jsonFile)

for projeto in data['projetos']:
    for servico in projeto['servicos']:
        # FrontOffice
        if "FrontOffice" in projeto['nome']:
            if servico['nome'] in projeto['plugins']:
                servico['caminho'] = data['base_url'] + data['frontoffice'] + data['frontoffice_front'] + data['plugins'] + servico['caminho_base']
            else:
                servico['caminho'] = data['base_url'] + data['frontoffice'] + servico['caminho_base']
        # BO
        if "BO" in projeto['nome']:
            if servico['nome'] in projeto['plugins']:
                servico['caminho'] = data['base_url'] + data['bo'] + data['bo_front'] + data['plugins'] + servico['caminho_base']
            else:
                servico['caminho'] = data['base_url'] + data['bo'] + servico['caminho_base']
    if "caminhoGulp" in projeto:
        if "FrontOffice" in projeto['nome']:
            projeto['caminhoGulp'] = data['base_url'] + data['frontoffice'] + data['frontoffice_front']
        if "BO" in projeto['nome']:
            projeto['caminhoGulp'] = data['base_url'] + data['bo'] + data['bo_front']

with open("caminhos.json", "w") as jsonFile:
    json.dump(data, jsonFile, indent=4)

input("Caminhos atualizados! Pressione ENTER para fechar esta janela.");

sys.exit();