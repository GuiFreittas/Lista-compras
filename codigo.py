class Time:
    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores

    def adiciona_jogador(self, nome, camisa):
        self.jogadores.append([nome, camisa])

    def imprime_jogadores(self):
        print(f"Jogadores do time {self.nome}:")
        for jogador in self.jogadores:
            print(f"{jogador[1]} - {jogador[0]}")

meu_time = Time("SC INTERNACIONAL", [["Guilherme", 10], ["Pedro Henrique", 25], ["De Pena", 1]])


meu_time.imprime_jogadores()


meu_time.adiciona_jogador("CR7", 7)


meu_time.imprime_jogadores()
