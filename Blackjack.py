from Jogo import Jogo
from Carta import Carta
from aux import cls, time, random

class Blackjack(Jogo):
    def __init__(self):
        self._jogador_mao = []
        self._dealer_mao = []
        self._aposta = 0
        self._parou = False

    def iniciar_jogo(self, aposta):
        cls()
        print("Dando as cartas...")
        self._jogador_mao = [self._comprar_carta() for _ in range(2)]
        self._dealer_mao = [random.choice(range(2,12)) for _ in range(2)]
        self._aposta = aposta
        self._parou = False
        time.sleep(2)
        cls()

    def mostrar_resultado(self):
        cls()
        jogador_total = sum(self._jogador_mao)
        dealer_total = sum(self._dealer_mao)
        print(f"Sua Mão: {self._jogador_mao} (Total: {jogador_total})")
        print(f"Mão do dealer: {self._dealer_mao} (Total: {dealer_total})")
        if jogador_total > 21:
            print("Jogador estourou! Dealer vence!")
            input("Pressione enter para sair")
            cls()
            return -self._aposta
        elif dealer_total > 21 or jogador_total > dealer_total:
            print("Você venceu!")
            input("Pressione enter para sair")
            cls()
            return self._aposta * 2
        elif jogador_total < dealer_total:
            print("Dealer vence!")
            time.sleep(3)
            cls()
            return -self._aposta
        else:
            print("Empate!")
            time.sleep(3)
            cls()
            return 0

    def jogar(self):
        while not self._parou:
            print(f"Sua mão atual: {self._jogador_mao} (Total: {sum(self._jogador_mao)})")
            escolha = input("Deseja puxar uma carta? (s/n): ").lower()
            if escolha == 's':
                self._jogador_mao.append(self._comprar_carta())
                if sum(self._jogador_mao) > 21:
                    break
            else:
                self._parou = True

    def dealer_jogar(self):
        while sum(self._dealer_mao) < 17:
            if sum(self._dealer_mao) <= 10:
                self._dealer_mao.append(random.choice(range(2,12)))

            elif random.choice([True, False]):
                self._dealer_mao.append(random.choice(range(2,12)))
            else:
                break

    def _comprar_carta(self):
        valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        naipes = ['Ouros', 'Paus', 'Copas', 'Espadas']
        carta = Carta(random.choice(valores), random.choice(naipes))
        carta.nome_carta()
        if carta.valor == 'A':
            return 11  
        elif carta.valor in ('J', 'Q', 'K'):
            return 10
        else:
            return carta.valor
