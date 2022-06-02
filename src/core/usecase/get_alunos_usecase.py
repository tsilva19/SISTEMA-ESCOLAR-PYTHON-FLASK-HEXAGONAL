from typing import Tuple, List

from jsonschema import ValidationError
from src.core.entity.dtos.alunos import AlunosDTO, ConsultaAlunos
from src.core.ports.get_alunos_port import GetAlunosPort


class GetAlunosUseCase:
    get_alunos_port = GetAlunosPort

    def __init__(self, get_alunos_port: GetAlunosPort) -> None:
        self.get_alunos_port = get_alunos_port

    def execute(self,
                alunos_dto: AlunosDTO) -> Tuple[List[ConsultaAlunos], int]:
        valida = alunos_dto.valida()

        if not valida.is_valid:
            raise ValidationError(valida.message)

        result = self.get_alunos_port.consulta(alunos_dto)
        return result if result else [], 200
