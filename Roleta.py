from Jogo import Jogo
from aux import cls, time, random

class Roleta(Jogo):
    def __init__(self):
        self._resultado = None
        self._aposta = 0
        self._numero_escolhido = None

    def iniciar_jogo(self, aposta):
        while True:
            try:
                cls()
                self._numero_escolhido = int(input("Escolha um número para apostar (0-36): "))
                if 0 <= self._numero_escolhido <= 36:
                    break
                print("Número inválido.")
            except ValueError:
                print("Entrada inválida.")
        self._resultado = random.randint(0, 36)
        self._aposta = aposta
        print("Girando a roleta...")
        time.sleep(3)
        cls()

    def mostrar_resultado(self):
        print(f"O resultado da roleta é: {self._resultado}")
        if self._resultado == self._numero_escolhido:
            print(f"Você ganhou {self._aposta * 10}! Parabéns!")
            input("Pressione enter para sair")
            cls()
            return self._aposta * 10
        print("Não foi dessa vez! Tente novamente!")
        input("Pressione enter para sair")
        cls()
        return -self._aposta
