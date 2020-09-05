from .flask_config import api
from controller.reclutadoridentificadorvalidar_controller import *

api.add_resource(ReclutadorIdentificadorValidarController,
    '/reclutador_identificador_validar')
