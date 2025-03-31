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
        



if __name__ == "__main__":
        pass
 