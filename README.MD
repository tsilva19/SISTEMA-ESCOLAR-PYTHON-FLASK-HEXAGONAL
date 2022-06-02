## PROJETO SISTEMA ESCOLA BACKEND FLASK HEXAGONAL


### REQUISITO

- possuir banco de dados mysql
- possuir linguagem python

### INstalação

- na raiz projeto digitar o comando para usar em ambiente virtual: ```python -m venv venv```

- habilitar o ambiente virtual com o comando: 
 -- para linux/git bash ``` source venv/Script/activate ```
 -- para windows/cmd ``` venv\Scripts\activate.bat ```

- instalação das bibliotecas:
 ```pip install -r requirements.txt ```

## START NO PROJETO

- Verifica se o arquivo .env existe no projeto e se o ambiente esta ativo digte o comando :
``` flask run ```

## comando para deletar entity

- yarn typeorm migration:revert

## USANDO a api 

- Acesse http://localhost:8082/alunos?id=1

![alt text](https://github.com/tsilva19/Injecao-Dependencia-node/blob/main/injetadependencia.png)

## FALANDO SOBRE ESTRUTURA HEXAGONAL

- Sobre a estrutura de pastas 

- adapter : são os adapatadores de entrada e saida pela qual na entrada possuo a pasta input que são recursos/dados que entraram na aplicação, e pasta output onde possui o recurso de banco de dados

- core : é a pasta onde possui as portas para interfaces, entity abstração para o banco de dados e usecases onde terá a logica de desenvolvimento do negocio.

- ports: ela faz comunicação entre adaptadores e o usecase

## DESENHO EXEMPLO HEXAGONAL
