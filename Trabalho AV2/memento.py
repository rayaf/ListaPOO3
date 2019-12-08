from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits
import random

class Robo():

    _velocidade = None
    _posicao = []

    def __init__(self, state: str, px: int, py: int) -> None:
        self._velocidade = state
        self._posicao = [px, py]
        print(f"Robo: minha velocidade e posição inicial é: {self._velocidade} e ({self._posicao[0]}x,{self._posicao[1]}y)")

    def do_something(self) -> None:

        print("Robo: mudando velocidade e posição.")
        self._velocidade = self._gerandor_de_velocidade()
        self._posicao = [self._gerandor_de_posicao(), self._gerandor_de_posicao()]
        print(f"Robo: velocidade e posição alterado para: {self._velocidade} e ({self._posicao[0]}x,{self._posicao[1]}y)")

    def _gerandor_de_velocidade(self) -> None:
        return str(random.randint(0,100)) + " Km"

    def _gerandor_de_posicao(self) -> None:
        return random.randint(0,15)

    def save(self) -> Memento:

        return ConcreteMemento(self._velocidade , self._posicao[0], self._posicao[1])

    def restore(self, memento: Memento) -> None:

        self._velocidade = memento.get_velocidade()
        print(f"Robo: velocidade e posição restaurada para: {self._velocidade} e ({self._posicao[0]}x, {self._posicao[1]})y")


class Memento(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str, px: int, py: int) -> None:
        self._velocidade = state
        self._posicao = [px,py]
        self._date = str(datetime.now())[:19]

    def get_velocidade(self) -> str:
        return self._velocidade

    def get_name(self) -> str:

        return f"{self._date} / ({self._velocidade[0:9]} ({self._posicao[0]},{self._posicao[1]}) ...)"

    def get_date(self) -> str:
        return self._date


class Caretaker():

    def __init__(self, robo: Robo) -> None:
        self._mementos = []
        self._robo = robo

    def backup(self) -> None:
        self._mementos.append(self._robo.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restaurando para: {memento.get_name()}")
        try:
            self._robo.restore(memento)
        except Exception:
            self.undo()
 
    def show_history(self) -> None:
        print("Caretaker: lista de mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    robo = Robo("3km", 5, 3)
    caretaker = Caretaker(robo)

    count = 0
    while (count < 6):
        caretaker.backup()
        robo.do_something()
        count += 1

    caretaker.backup()

    print()
    caretaker.show_history()

    count = 0
    while (count < 5):
        print("\nDesfazendo a operação\n")
        caretaker.undo()
        count += 1
    print("\nDesfazendo a operação pela quinta vez\n")
    caretaker.undo()