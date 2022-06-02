from flask_cors import CORS
from flask import Flask
from src.adapter.input.controller.alunos_controller import Alunos
from src.trata_erro import Api

app = Flask(__name__)
CORS(app)
api = Api(app)
api.add_resource(Alunos, "/alunos")
