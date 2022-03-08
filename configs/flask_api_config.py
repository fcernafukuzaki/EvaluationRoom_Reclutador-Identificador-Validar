from .flask_config import api
from controller.reclutadoridentificadorvalidar_controller import *
from controller.reclutadoremailvalidar_controller import *

api.add_resource(ReclutadorIdentificadorValidarController,
    '/reclutador_identificador_validar')

api.add_resource(ReclutadorEmailValidarController,
    '/reclutador_email_validar')