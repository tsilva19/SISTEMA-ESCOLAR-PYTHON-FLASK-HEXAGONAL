import json
import logging
from flask_restful import Resource
from flask import Response, request
from src.adapter.output.database.alunos_repository import AlunosRepository
from src.core.entity.dtos.alunos import AlunosDTO

from src.core.usecase.get_alunos_usecase import GetAlunosUseCase


class Alunos(Resource):
    def get(self):
        try:
            args = request.args
            print(f"Obtendo informações: {args}")
            get_alunos_usecase = GetAlunosUseCase(get_alunos_port=AlunosRepository())
            result, status_code = get_alunos_usecase.execute(AlunosDTO(**args))

            return Response(
                response=json.dumps(result, default=lambda element: element.__dict__),
                status=status_code,
                content_type="application/json",
            )
        except Exception as error:
            logging.error("Erro ao tentar executar", str(error))
