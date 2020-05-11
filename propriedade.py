# -*- Coding: UTF-8 -*-

class Propriedades():
    def __init__(self, nome, valor_venda, aluguel, proprietario=None):
        self.nome = nome
        self.valor_venda = valor_venda
        self.aluguel = aluguel
        self.proprietario = proprietario

    def disponivel_compra(self):
        ''' Metodo que verifica se a propriedade tem dono.
        '''
        if self.proprietario:
            return False
        return True

    def comprar(self, possivel_dono):
        ''' Metodo que faz a compra do imovel verificando se o possivel dono
        tem a quantia ou se a propriedade tem proprietario.
        Se acaso não atender nenhuma dessas condições o jogador entre na verificação 
        de pagamento de aluguel.
        '''
        if self.disponivel_compra():
            if possivel_dono.proprietario_tem_quantia(self.valor_venda):
                possivel_dono.subtrair_valor(self.valor_venda)
                self.proprietario = possivel_dono
                return True
        else:
            self.pagar_aluguel(possivel_dono)

    def pagar_aluguel(self, jogador):
        ''' Metodo que realiza a combrança do aluguel o jogador que não é proprietario.
        ''' 
        if jogador.jogando == True:
            if not self.disponivel_compra() and not jogador.nome == self.proprietario.nome:
                jogador.subtrair_valor(self.aluguel)
                self.proprietario.valor_total += self.aluguel

    def volta_banco(self):
        ''' Metodo que devolve a propriedade para o banco.
        '''
        self.proprietario = None
        return True