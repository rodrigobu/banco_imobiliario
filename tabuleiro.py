# -*- Coding: UTF-8 -*-
import random

from estrategia import JogadorAleatorio, JogadorCauteloso, JogadorExigente
from estrategia import JogadorImpulsivo
from propriedade import Propriedades
from dicionario_propriedaes import PROPRIEDADES


class Tabuleiro():
    
    def __init__(self):
        self.propriedades = []
        self.jogadores = []

    def add_propriedades(self):
        ''' Metodo que adiciona as propriedades no tabuleiro.
        '''
        propriedades = dict()
        indice = 1
        for p in PROPRIEDADES:
            propriedade = Propriedades(
                nome=p.get('nome'),
                valor_venda=p.get('venda'),
                aluguel=p.get('aluguel'),
                proprietario=p.get('dono')
            )
            propriedades[indice] = propriedade
            indice += 1
            
        self.propriedades.append(propriedades)

    def add_jogador(self):
        ''' Metodo adiciona os jogadores com seus comportamentos exclusivos
        '''
        self.jogadores.append(JogadorAleatorio('Aleatorio'))
        self.jogadores.append(JogadorCauteloso('Cauteloso'))
        self.jogadores.append(JogadorExigente('Exigente'))
        self.jogadores.append(JogadorImpulsivo('Impulsivo'))

    def shuffle_jogador(self):
        ''' Metodo que embaralhar os jogodores.
        '''
        random.shuffle(self.jogadores) 

    def jogadores_ativo(self):
        ''' Metodo que retorna uma lista de jogadores ativos.
        '''
        ativo = []
        for jogador in self.jogadores:
            if jogador.jogando:
                ativo.append(jogador)
        return ativo       

    def jogadores_inativo(self):
        ''' Metodo que retorna uma lista de inativo.
        '''
        jogadores_inativo = filter(lambda x: x.jogando == False, self.jogadores)
        return jogadores_inativo       
    
    def organizando_tabuleiro(self):
        self.add_jogador()
        self.add_propriedades()        
    
    def devolver_propriedades_jogador(self):
        ''' Metodo que devolve as propriedades para banco quando o
        jogador sai da partida.
        '''
        jogador = self.jogadores_inativo()
        propriedades = self.propriedades[0]
        for j in jogador:
            for k,v in propriedades.items():
                if not v.proprietario is None:
                    if propriedades[k].proprietario == j:
                        propriedades[k].volta_banco()

    def devolver_propriedades(self):
        ''' Metodo que devolve todas as propriedades para banco
        '''
        propriedades = self.propriedades[0]
        for k,v in propriedades.items():
            propriedades[k].volta_banco()
    
    def resetar_jogadores(self):
        ''' Metodo que deixa todos os jogadores com seus valores
        default.
        '''
        for jogador in self.jogadores:
            jogador.resetar_jogador()
        
       
    def novo_tabuleiro(self):
        ''' Metodo utilizado para iniciar um nova partida
        '''
        self.devolver_propriedades()
        self.resetar_jogadores()
        self.shuffle_jogador()