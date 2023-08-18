class SistemaOperacional:
    def __init__(self, nome, versao):
        self.nome = nome
        self.versao = versao

class Computador:
    def __init__(self, sistema):
        self.sistema = sistema

sistema_windows = SistemaOperacional(nome="Windows", versao="10")
meu_computador = Computador(sistema=sistema_windows)

print(f"Meu computador está rodando {meu_computador.sistema.nome} {meu_computador.sistema.versao}")
