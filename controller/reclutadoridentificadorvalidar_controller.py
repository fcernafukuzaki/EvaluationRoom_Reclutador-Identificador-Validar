from flask import request
from flask_restful import Resource
from configs.flask_config import app
from service.reclutadoridentificadorvalidar_service import ReclutadorIdentificadorValidarService
from service.autorizador_service import AutorizadorService
from object.usuario import Usuario, UsuarioSchema

reclutadoridentificadorvalidar_service = ReclutadorIdentificadorValidarService()
autorizador_service = AutorizadorService()
usuario_schema = UsuarioSchema()


class ReclutadorIdentificadorValidarController(Resource):

    def post(self):
        token = request.json['Authorization']
        email_reclutador = request.json['correoelectronico']

        email_valido, mensaje, usuario = reclutadoridentificadorvalidar_service.valida_email_reclutador(email_reclutador)
        if email_valido:
            valido = autorizador_service.validar_token(token, usuario.idusuario)
            if valido:
                return usuario_schema.jsonify(usuario)
            return {'mensaje': 'Operación no valida.'}, 403
        return {'mensaje': mensaje}, 404