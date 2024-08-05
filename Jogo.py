from abc import ABC, abstractmethod

class Jogo(ABC):
    @abstractmethod
    def iniciar_jogo(self, aposta):
        pass

    @abstractmethod
    def mostrar_resultado(self):
        pass  

