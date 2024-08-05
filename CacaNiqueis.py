from Jogo import Jogo
from aux import cls, time, random

class CacaNiqueis(Jogo):
    PRÊMIO = 10000

    def __init__(self):
        self._resultado = []
        self._aposta = 200
    
    def iniciar_jogo(self, aposta):
        cls()
        self._resultado = [random.choice('♠❤☂☠♦') for _ in range(3)]
        print("Girando os rolos...")
        time.sleep(2)
        cls()

    def mostrar_resultado(self):
        print(f"O resultado dos rolos é: {self._resultado}")
        if len(set(self._resultado)) == 1:
            print(f"Você ganhou! Seu prêmio é: {self.PRÊMIO}")
            return self.PRÊMIO
        print(f"Você perdeu! Você perdeu sua aposta de: {self._aposta}")
        input("Pressione enter para sair.")
        cls()
        return -self._aposta

