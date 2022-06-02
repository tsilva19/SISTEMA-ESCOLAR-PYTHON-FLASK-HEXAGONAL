from dataclasses import dataclass
from datetime import date

from typing import Optional, Union, List


@dataclass
class ValidaTipo:
    is_valid: bool
    message: Optional[str] = None


@dataclass
class UtilsAlunosDTO:
    def get_dict(self) -> dict:
        return self.__dict__

    def parse_to_int(self, input) -> Union[int, None]:
        return int(input) if input else None

    def valida(self, campos: List[str]) -> ValidaTipo:
        for campo in campos:
            valor = getattr(self, campo)

            if valor is None:
                return ValidaTipo(
                    is_valid=False, message=f"atributo requerido: {campo}"
                )

            if isinstance(valor, list) and not len(valor):
                return ValidaTipo(
                    is_valid=False,
                    message=(f"{campo} deve conter ao menos um valor"),
                )
        return ValidaTipo(is_valid=True)


@dataclass
class AlunosDTO(UtilsAlunosDTO):
    def __init__(self, **kwargs) -> None:
        self.id: int = kwargs.get("id")
        self.cpf: chr = kwargs.get("cpf")
        self.nome: str = kwargs.get("nome")
        self.data_nascimento: date = kwargs.get("data_nascimento")

    def valida(self) -> ValidaTipo:
        campos = ["id"]
        return super().valida(campos)


@dataclass
class ConsultaAlunos:
    def __init__(
        self,
        id: int,
        cpf: chr,
        nome: str,
        email: str,
        fone: chr,
        data_nascimento: date
    ):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.fone = fone
        self.data_nascimento = data_nascimento

    def get_dict(self):
        return self.__dict__
