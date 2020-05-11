# -*- Coding: UTF-8 -*-

import random

class Jogador():
    ''' Classe utilizada para definir ações do jogador
    '''
    def __init__(self, nome, valor_inicial=300.00):
        self.nome = nome
        self.valor_total = valor_inicial
        self.jogando = True
        self.posicao_tab = 0
        self.valor_inicial = valor_inicial

    def subtrair_valor(self, valor_montante):
        ''' Metodo utilizado para subtrair o valor do jogador
        '''
        self.valor_total -= valor_montante
        if self.valor_total <= 0:
            self.remover_jogador()
    
    def proprietario_tem_quantia(self, valor_nesce):
        ''' Metodo que verifica se o jogador tem a quantia
        nescessaria para executar a ação
        '''
        if self.valor_total >= valor_nesce:
            return True
        return False

    def remover_jogador(self):
        ''' Metodo que remove o jogado se ele zerar o saldo.
        '''
        if self.valor_total <= 0:
            self.jogando = False
        return self.jogando

    def resetar_jogador(self):
        ''' Metodo utilizado para reiniciar os status do jogadores
        '''
        self.jogando = True
        self.valor_total = self.valor_inicial
        self.posicao_tab = 0

    def andar(self):
        ''' Metodo utilizando para executar ação de jogar dados e andar 
        as casas do tabuleiro de acordo com a numeração do dado.
        Só os jogadores que estiveram com status jogando == True pode executar
        esse metodo.
        '''
        jogar_dados = random.choice(range(1,7))
        if self.jogando == True:
            self.posicao_tab += jogar_dados
            if self.posicao_tab > 19:
                self.valor_total += 100
                self.posicao_tab -= 19

        return self.posicao_tab
