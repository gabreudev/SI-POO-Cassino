class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def nome_carta(self):
        print(f"Você puxou um {self.valor} de {self.naipe}")
