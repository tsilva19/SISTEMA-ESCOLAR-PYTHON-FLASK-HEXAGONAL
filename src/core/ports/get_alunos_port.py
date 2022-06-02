from abc import abstractmethod
from typing import Optional
from src.core.entity.dtos.alunos import AlunosDTO, ConsultaAlunos


class GetAlunosPort:
    @abstractmethod
    def consulta(self, alunosdto: AlunosDTO) -> Optional[ConsultaAlunos]:
        raise NotImplementedError
