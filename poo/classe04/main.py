class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        valor = valor.title()
        self._nome = valor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor


p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.preco)
print(p1.nome)

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.preco)
