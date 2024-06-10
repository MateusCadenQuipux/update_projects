import os
import subprocess
import logging
import sys
import json

logger = logging.getLogger(__name__)
logging.basicConfig(filename='update.log', level=logging.INFO, filemode="w")
logger.info('Started')

with open("../paths/caminhos.json", "r") as jsonFile:
    data = json.load(jsonFile)

projetos = data['projetos']

# Frontoffice Backend
# servicios_frontoffice_back = []
# servicios_frontoffice_back.extend([
# {
    # "nome": "Transversal",
    # "caminho": base_url + url_sistema['frontoffice'] + "/utilidades/transversal",
    # "branch": "development"
# },
# {
    # "nome": "Conf",
    # "caminho": base_url + url_sistema['frontoffice'] + "/conf/conf",
    # "branch": "development"
# },
# {
    # "nome": "Core",
    # "caminho": base_url + url_sistema['frontoffice'] + "/plugin-core-backend-qits2",
    # "branch": "development"
# },
# {
    # "nome": "Commons",
    # "caminho": base_url + url_sistema['frontoffice'] + "/plugin-commons-backend",
    # "branch": "Feature_Registrar_Etapa_Externa_Solicitud"
# },
# {
    # "nome": "Alertas",
    # "caminho": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front'] + url_sistema['plugins'] + "/plugin-alertas-frontoffice/alertas-backend",
    # "branch": "development"
# },
# {
    # "nome": "Gestion atencion",
    # "caminho": base_url + url_sistema['frontoffice'] + "/plugin-gestion-atencion-backoffice/gestion-atencion-backoffice-backend",
    # "branch": "development"
# },
# {
    # "nome": "Integrador qxtransito",
    # "caminho": base_url + url_sistema['frontoffice'] + "/plugin-integrador-qxtransito",
    # "branch": "development"
# },
# {
    # "nome": "Login BDJWT",
    # "caminho": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front'] + url_sistema['plugins'] + "/plugin-login-bdjwt/login-bdjwt-backend",
    # "branch": "development"
# },
# {
    # "nome": "Registro ciudadano Brasil",
    # "caminho": base_url + url_sistema['frontoffice'] + "/plugin-registro-ciudadano-brasil-backend",
    # "branch": "development"
# },
# {
    # "nome": "Servicios digitales",
    # "caminho": base_url + url_sistema['frontoffice'] + "/plugin-servicios-digitales-backoffice-brasil/servicios-digitales-backoffice-backend",
    # "branch": "development"
# },
# {
    # "nome": "Base back qits2",
    # "caminho": base_url + url_sistema['frontoffice'] + "/base-back-qits2/basebackqits2parent",
    # "branch": "development"
# }
# ])

# projetos.append({ 
    # "nome": "FrontOffice - Back",
    # "servicos": servicios_frontoffice_back
# })

# Frontoffice Frontend
# servicios_frontoffice_front = []
# servicios_frontoffice_front.extend([
# {
    # "nome": "Plugin alertas",
    # "caminho": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front'] + url_sistema['plugins'] + "/plugin-alertas-frontoffice/alertas-frontend",
    # "branch": "development"
# },
# {
    # "nome": "Plugin alertas frontoffice",
    # "caminho": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front'] + url_sistema['plugins'] + "/plugin-alertas-frontoffice-frontend-brasil",
    # "branch": "development"
# },
# {
    # "nome": "Plugin gestion atencion",
    # "caminho": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front'] + url_sistema['plugins'] + "/plugin-gestion-atencion-frontoffice-frontend",
    # "branch": "development"
# },
# {
    # "nome": "Plugin home shopping",
    # "caminho": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front'] + url_sistema['plugins'] + "/plugin-home-shopping-frontoffice",
    # "branch": "development"
# },
# {
    # "nome": "Plugin login bdjwt",
    # "caminho": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front'] + url_sistema['plugins'] + "/plugin-login-bdjwt/login-bdjwt-frontend",
    # "branch": "development"
# },
# {
    # "nome": "Plugin login brasil",
    # "caminho": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front'] + url_sistema['plugins'] + "/plugin-login-brasil-frontoffice-frontend",
    # "branch": "development"
# },
# {
    # "nome": "Plugin registro ciudadano",
    # "caminho": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front'] + url_sistema['plugins'] + "/plugin-registro-ciudadano-shopping-frontoffice-frontend",
    # "branch": "development"
# },
# {
    # "nome": "Plugin solicitudes",
    # "caminho": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front'] + url_sistema['plugins'] + "/plugin-solicitudes-frontoffice/solicitudes-frontend",
    # "branch": "development"
# },
# {
    # "nome": "Plugin solicitudes shopping",
    # "caminho": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front'] + url_sistema['plugins'] + "/plugin-solicitudes-shopping-frontoffice-frontend/solicitudes-shopping-frontoffice-frontend",
    # "branch": "development"
# }
# ])

# projetos.append({ 
    # "nome": "FrontOffice - Front",
    # "servicos": servicios_frontoffice_front,
    # "caminhoGulp": base_url + url_sistema['frontoffice'] + url_sistema['frontoffice_front']
# })

# BO Back
# servicios_bo_back = []
# servicios_bo_back.extend([
# {
    # "nome": "Transversal",
    # "caminho": base_url + url_sistema['bo'] + "/utilidades/transversal",
    # "branch": "development"
# },
# {
    # "nome": "Conf",
    # "caminho": base_url + url_sistema['bo'] + "/conf/conf",
    # "branch": "development"
# },
# {
    # "nome": "Core",
    # "caminho": base_url + url_sistema['bo'] + "/plugin-core-backend-qits2",
    # "branch": "development"
# },
# {
    # "nome": "Commons",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-commons-backend",
    # "branch": "Feature_Registrar_Etapa_Externa_Solicitud"
# },
# {
    # "nome": "Login",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-login-backoffice/login-backoffice-backend",
    # "branch": "development"
# },
# {
    # "nome": "Integrador qxtransito",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-integrador-qxtransito",
    # "branch": "development"
# },
# {
    # "nome": "Administracion seguridad",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-administracion-seguridad-backoffice/administracion-seguridad-backend",
    # "branch": "development"
# },
# {
    # "nome": "Turnos",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-visualizacion-atencion-backoffice/turnos-backend",
    # "branch": "development"
# },
# {
    # "nome": "Gestion atencion",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-gestion-atencion-backoffice/gestion-atencion-backoffice-backend",
    # "branch": "development"
# },
# {
    # "nome": "Common SSDD",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-common-ssdd-backoffice/common-ssdd-backend",
    # "branch": "brasil"
# },
# {
    # "nome": "Servicios digitales",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-servicios-digitales-backoffice-brasil/servicios-digitales-backoffice-backend",
    # "branch": "development"
# },
# {
    # "nome": "Gestor servicio Brasil",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-gestor-servicio-brasil-backoffice/gestor-servicio-brasil-backend",
    # "branch": "development"
# },
# {
    # "nome": "Registro ciudadano Brasil",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-registro-ciudadano-brasil-backend",
    # "branch": "development"
# },
# {
    # "nome": "Base back qits2",
    # "caminho": base_url + url_sistema['bo'] + "/base-back-qits2/basebackqits2parent",
    # "branch": "development"
# }
# ])

# projetos.append({ 
    # "nome": "BO - Back",
    # "servicos": servicios_bo_back
# })

# BO Front
# servicios_bo_front = []
# servicios_bo_front.extend([
# {
    # "nome": "Administracion seguridad",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-administracion-seguridad-backoffice/administracion-seguridad-frontend",
    # "branch": "development"
# },
# {
    # "nome": "Common SSDD",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-common-ssdd-backoffice/common-ssdd-frontend",
    # "branch": "brasil"
# },
# {
    # "nome": "Commons backend",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-commons-backend",
    # "branch": "Feature_Registrar_Etapa_Externa_Solicitud"
# },
# {
    # "nome": "Gestion atencion",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-gestion-atencion-backoffice/gestion-atencion-backoffice-frontend",
    # "branch": "development"
# },
# {
    # "nome": "Gestor servicio Brasil",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-gestor-servicio-brasil-backoffice/gestor-servicio-brasil-frontend",
    # "branch": "development"
# },
# {
    # "nome": "Integrador qxtransito",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-integrador-qxtransito",
    # "branch": "development"
# },
# {
    # "nome": "Login backoffice",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-login-backoffice/login-backoffice-frontend",
    # "branch": "development"
# },
# {
    # "nome": "Registro ciudadano Brasil",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-registro-ciudadano-brasil-backend",
    # "branch": "development"
# },
# {
    # "nome": "Servicios digitales",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-servicios-digitales-backoffice-brasil/servicios-digitales-backoffice-frontend",
    # "branch": "development"
# },
# {
    # "nome": "Turnos",
    # "caminho": base_url + url_sistema['bo'] + url_sistema['bo_front'] + url_sistema['plugins'] + "/plugin-visualizacion-atencion-backoffice/turnos-frontend",
    # "branch": "development"
# }
# ])

# projetos.append({ 
    # "nome": "BO - Front",
    # "servicos": servicios_bo_front,
    # "caminhoGulp": base_url + url_sistema['bo'] + url_sistema['bo_front']
# })

# Rodar git pulls
for projeto in projetos:
    print("Atualizando: " + projeto['nome'])
    logger.info("---------- Projeto: " + projeto['nome'] + "----------\n")
    for index, servico in enumerate(projeto['servicos']):
        try:
            subprocess.check_output(["git", "checkout", servico['branch']], shell=True, stderr=subprocess.STDOUT, universal_newlines=True, cwd=servico['caminho'])
            saida_log = subprocess.check_output(["git", "pull", "origin", servico['branch']], shell=True, stderr=subprocess.STDOUT, universal_newlines=True, cwd=servico['caminho'])
            logger.info(servico['nome'] + " - OK")
            print(servico['nome'] + " - OK (" + str(index + 1) + "/" + str(len(projeto['servicos'])) + ")")
            logger.info("\n" + saida_log + "\n")
        except subprocess.CalledProcessError as e:
            print(servico['nome'] + " - ERROR! (" + str(index + 1) + "/" + str(len(projeto['servicos'])) + ")")
            if "fatal: unable to access" in e.output:
                print("Sem acesso ao repositório, verificar VPN!")
            logger.error(servico['nome'] + " - ERROR")
            logger.error("\n" + e.output)
    # gulp dist
    if "caminhoGulp" in projeto:
        try:
            print("Realizando gulp dist...")
            saida_log = subprocess.check_output(["gulp", "dist"], shell=True, stderr=subprocess.STDOUT, universal_newlines=True, cwd=projeto['caminhoGulp'])
            print("Gulp dist OK")
            logger.info(projeto['nome'] + " - Gulp OK")
            logger.info("\n" + saida_log + "\n")
        except subprocess.CalledProcessError as e:
            print(projeto['nome'] + " - Gulp ERROR!")
            logger.error(projeto['nome'] + " - Gulp ERROR")
            logger.error("\n" + e.output)
    print("\n")


input("Projetos atualizados! Pressione Enter para fechar esta janela. ")
sys.exit();