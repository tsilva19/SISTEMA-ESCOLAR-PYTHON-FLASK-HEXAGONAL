class ErroServidor(Exception):
    def __init__(self, message: str = "Erro interno no servidor"):
        self.message = message
        super().__init__(self.message)
