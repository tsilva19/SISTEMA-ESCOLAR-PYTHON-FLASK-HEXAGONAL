from flask_restful import Api as _Api
from typing import Dict
from werkzeug.exceptions import NotFound
from src.exceptions.not_found import NaoEncontrado
from src.exceptions.erro_servidor import ErroServidor
from src.exceptions.valida_erro import ValidaErro


class Api(_Api):
    def error_router(self, original_handler, error):
        if isinstance(error, ValidaErro):
            return handle_validation_error(error)
        if isinstance(error, NaoEncontrado):
            return handle_not_found_error(NotFound())
        if isinstance(error, ErroServidor):
            return handle_server_error(error)
        return original_handler(error)


def build_message_error(error_message: str) -> Dict[str, str]:
    return {"message": f"{error_message}"}


def handle_validation_error(error: ValidaErro):
    return build_message_error(error.message), 400


def handle_not_found_error(error: NotFound):
    return build_message_error(error.message), 404


def handle_server_error(error: ErroServidor):
    return build_message_error(error.message), 400
