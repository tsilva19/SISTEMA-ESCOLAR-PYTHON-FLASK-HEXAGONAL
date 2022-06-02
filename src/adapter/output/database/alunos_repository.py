import logging
from typing import List, Optional
from src.adapter.output.database.mysql import Mysql
from src.core.entity.dtos.alunos import AlunosDTO, ConsultaAlunos
from src.core.ports.get_alunos_port import GetAlunosPort


class AlunosRepository(GetAlunosPort):
    def consulta(self,
                 alunos_dto: AlunosDTO) -> Optional[List[ConsultaAlunos]]:
        try:
            query_string = f"""
                  select
                    id as id,
                    cpf as cpf,
                    nome as nome,
                    email as email,
                    fone as fone,
                    cast(data_nascimento as char) as data_nascimento
                  from alunos
                    where id = {alunos_dto.id}
            """

            print(query_string)
            result = Mysql.fetchall(sql=query_string)
            print(result)
            return (
                [ConsultaAlunos(**alunos) for alunos in result]
                if len(result) else None
            )

        except Exception as e:
            logging.error("Erro na consulta do bano de dados", e)
