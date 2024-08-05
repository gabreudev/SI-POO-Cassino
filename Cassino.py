from Roleta import Roleta
from CacaNiqueis import CacaNiqueis
from CorridaDeCavalos import CorridaDeCavalos
from Blackjack import Blackjack

from aux import cls
    

class Cassino:
    def __init__(self):
        self._jogos = {
            'roleta': Roleta(),
            'blackjack': Blackjack(),
            'caca_niqueis': CacaNiqueis(),
            'corrida_de_cavalos': CorridaDeCavalos()
        }
        self._dinheiro = 5000

    def exibir_menu(self):
        while self._dinheiro > 0:
            print(f"\nSaldo: {self._dinheiro}")
            print("1. Roleta")
            print("2. Blackjack")
            print("3. Caça-Níqueis")
            print("4. Corrida de Cavalos")
            print("5. Sair")
            escolha = input("Escolha um jogo: ")

            if escolha == '1':
                self.jogar_jogo('roleta')
            elif escolha == '2':
                self.jogar_jogo('blackjack')
            elif escolha == '3':
                self.jogar_jogo('caca_niqueis')
            elif escolha == '4':
                self.jogar_jogo('corrida_de_cavalos')
            elif escolha == '5':
                print("Obrigado e volte sempre!")
                break
            else:
                cls()
                print("Escolha invalida.")

        if self._dinheiro <= 0:
            print("Você ficou sem dinheiro! Volte quando puder jogar.")

    def jogar_jogo(self, jogo_nome):
        if jogo_nome == 'caca_niqueis':
            aposta = 200
        else:
            while True:
                try:
                    aposta = int(input(f"Você tem {self._dinheiro}. Quanto deseja apostar? "))
                    if 0 < aposta <= self._dinheiro:
                        break
                    print("Valor invalido.")
                except ValueError:
                    print("Opção invalida.")

        jogo = self._jogos.get(jogo_nome)
        if jogo:
            jogo.iniciar_jogo(aposta)
            if jogo_nome == 'blackjack':
                jogo.jogar()
                jogo.dealer_jogar()
            resultado = jogo.mostrar_resultado()
            self._dinheiro += resultado
        else:
            print("Jogo não encontrado.")
