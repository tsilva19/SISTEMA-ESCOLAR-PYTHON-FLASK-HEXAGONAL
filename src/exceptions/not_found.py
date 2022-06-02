class NaoEncontrado(Exception):
    def __init__(self, message: str = "Recurso não encontrado"):
        self.message = message
        super().__init__(self.message)
