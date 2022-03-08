from configs.flask_config import db
from object.login_user import LoginUser


class AutorizadorService:

    @staticmethod
    def validar_token(hash, idusuario):
        if hash:
            return db.session.query(LoginUser
                ).filter(LoginUser.hash == hash,
                         LoginUser.date_logout == None,
                         LoginUser.iduser == idusuario
                         ).first()
        return False
