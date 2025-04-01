class Produto:
    def __init__(self, nome=str, preco=float, estoque=int, peso_kg=float):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.peso_kg = peso_kg

    def atualizar_preco(self, novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco

    def aplicar_desconto(self, percentual):
        percentual = 1 - (percentual/100)
        self.preco = self.preco * percentual

    def verificar_estoque_baixo(self):
        if self.estoque < 5:
            return True
        return False

    def __eq__(self, Q2):
        return self.nome == Q2.nome and self.preco == Q2.preco

    def __str__(self):
        return (f"Produto: {self.nome} | Preço: R$ {self.preco} | Estoque: {self.estoque}")


class Cliente:
    def __init__(self, nome=str, email=str, pontos_fidelidade=int):
        self.nome = nome
        self.email = email
        self.pontos_fidelidade = 0

    def adicionar_pontos(self, pontos):
        if pontos > 0:
            self.pontos_fidelidade = pontos

    def resgatar_pontos(self, pontos):
        if pontos > 0:
            self.pontos_fidelidade -= pontos

    def verificar_vip(self):
        if self.pontos_fidelidade >= 1000:
            return True
        return False

    def __eq__(self, Q2):
        return self.email == Q2.email

    def __iadd__(self, pontos=int):
        if pontos > 0:
            self.pontos_fidelidade += pontos

    def __str__(self):
        return (f"Cliente: {self.nome} | Pontos: {self.pontos_fidelidade}")


if __name__ == "__main__":
    pass