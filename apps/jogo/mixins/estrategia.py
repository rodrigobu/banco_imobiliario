# -*- Coding: UTF-8 -*-

import random

from apps.jogo.mixins.jogador import Jogador

class JogadorImpulsivo(Jogador):
    ''' Class que herda a classe de Jogador para adicionar 
    comportamente ao jogador.
    '''
    def oportunidade_compra(self, propriedade):
        if (self.valor_total >= propriedade.valor_venda):

            propriedade.comprar(self)
            return True
        else:
            propriedade.pagar_aluguel(self)
            return False


class JogadorCauteloso(Jogador):
    ''' Class que herda a classe de Jogador para adicionar 
    comportamente ao jogador.
    '''
    def oportunidade_compra(self, propriedade):
        if ((self.valor_total - 80) >= propriedade.valor_venda):
            propriedade.comprar(self)
            return True
        else:
            propriedade.pagar_aluguel(self)
            return False



class JogadorExigente(Jogador):
    ''' Class que herda a classe de Jogador para adicionar 
    comportamente ao jogador.
    '''
    def oportunidade_compra(self, propriedade):
        if (self.valor_total >= propriedade.valor_venda and propriedade.valor_venda > 50):
            propriedade.comprar(self)
            return True
        else:
            propriedade.pagar_aluguel(self)
            return False



class JogadorAleatorio(Jogador):
    ''' Class que herda a classe de Jogador para adicionar 
    comportamente ao jogador.
    '''
    def oportunidade_compra(self, propriedade):
        if (self.valor_total >= propriedade.valor_venda and random.choice([True, False])):
            propriedade.comprar(self)
            return True
        else:
            propriedade.pagar_aluguel(self)
            return False