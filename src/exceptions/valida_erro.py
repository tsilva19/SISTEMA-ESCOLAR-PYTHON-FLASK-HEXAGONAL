class ValidaErro(Exception):
    def __init__(self, message: str = "Erro de validação"):
        self.message = message
        super().__init__(self.message)
