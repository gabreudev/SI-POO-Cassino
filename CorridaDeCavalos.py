from Jogo import Jogo
from aux import cls, time, random

class CorridaDeCavalos(Jogo):
    def __init__(self):
        self._resultado = None
        self._aposta = 0
        self._cavalo_escolhido = None
        
        self._nomes_cavalos = {
            1: "Bolacha",
            2: "Zambeta",
            3: "Pé de pano",
            4: "Ferrugem",
            5: "Cenoura"
        }

    def iniciar_jogo(self, aposta):
        while True:
            try:
                cls()
                print("Tabela de Cavalos:")
                for numero, nome in self._nomes_cavalos.items():
                    print(f"Cavalo {numero}: {nome}")
                
                self._cavalo_escolhido = int(input("Escolha um cavalo para apostar: "))
                if 1 <= self._cavalo_escolhido <= 5:
                    break
                print("Número inválido.")
            except ValueError:
                print("Entrada inválida.")
        
        self._aposta = aposta
        nome_cavalo_escolhido = self._nomes_cavalos[self._cavalo_escolhido]
        print(f"Você apostou no cavalo {self._cavalo_escolhido}: {nome_cavalo_escolhido}")
        print("Corrida começando...")
        time.sleep(2)
        cls()
        self._resultado = self.simular_corrida()

    def simular_corrida(self):
        cavalos = [1, 2, 3, 4, 5]
        print("Cavalos correndo...")
        num_trocas = random.randint(5,20) 
        for i in range(num_trocas):
            time.sleep(1.5)  
            cls()
            self._trocar_posicoes(cavalos)
            posicoes = [f"{self._nomes_cavalos[num]} ({num})" for num in cavalos]
            print("Posições atuais dos cavalos:")
            for j, nome in enumerate(posicoes, start=1):
                print(f"{j}º - {nome}")

        self._resultado = cavalos[0]
        return self._resultado

    def _trocar_posicoes(self, cavalos):
        for i in range(len(cavalos) - 1):
            if random.choice([True, False]):
                if i < len(cavalos) - 1:
                    cavalos[i], cavalos[i + 1] = cavalos[i + 1], cavalos[i]

    def mostrar_resultado(self):
        nome_resultado = self._nomes_cavalos[self._resultado]
        print(f"O cavalo vencedor é: {self._resultado} - {nome_resultado}")
        if self._resultado == self._cavalo_escolhido:
            print(f"Você ganhou! Seu prêmio é: {self._aposta * 5}")
            input("Pressione enter para sair")
            cls()
            return self._aposta * 10
        print(f"Você perdeu! Você perdeu sua aposta de: {self._aposta}")
        input("Pressione enter para sair")    
        cls()
        return -self._aposta
