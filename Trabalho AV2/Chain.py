from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any, valor) -> str:
        if self._next_handler:
            return self._next_handler.handle(request, valor)

        return None

class bBHandler(AbstractHandler):
    def handle(self, request: Any, valor) -> str:
        if request == "001":
            return f"Transferencia no valor de {valor} realizada com sucesso"
        else:
            return super().handle(request, valor)


class caixaHandler(AbstractHandler):
    def handle(self, request: Any, valor) -> str:
        if request == "104":
            return f"Transferencia no valor de {valor} realizada com sucesso"
        else:
            return super().handle(request, valor)


class bradescoHandler(AbstractHandler):
    def handle(self, request: Any, valor) -> str:
        if request == "237":
            return f"Transferencia no valor de {valor} realizada com sucesso"
        else:
            return super().handle(request, valor)

class santanderHandler(AbstractHandler):
    def handle(self, request: Any, valor) -> str:
        if request == "033":
            return f"Transferencia no valor de {valor} realizada com sucesso"
        else:
            return super().handle(request, valor)


def client_code(handler: Handler, numeroDaAgencia, valor) -> None:
      print(f"\nTransferencia para agencia {numeroDaAgencia}")
      result = handler.handle(numeroDaAgencia, valor)
      if result:
          print(f"  {result}", end="")
      else:
          print(f" Agencia {numeroDaAgencia} não está cadastrada", end="")


if __name__ == "__main__":
    bancoDoBrasil = bBHandler()
    caixa = caixaHandler()
    bradesco = bradescoHandler()
    santander = santanderHandler()


    bancoDoBrasil.set_next(caixa).set_next(bradesco).set_next(santander)

    print("Bancos: Banco Do Brasil > Caixa > Bradesco > Santander")
    numeroDaAgencia = input('entre com o numero da agencia: ')
    valor = int(input('entre com o valor a ser transfeido: '))
    client_code(bancoDoBrasil, numeroDaAgencia, valor)