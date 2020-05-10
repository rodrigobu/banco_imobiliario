import random

class Jogador():

    def __init__(self, nome, valor_inicial=600.00):
        self.nome = nome
        self.valor_total = valor_inicial
        self.jogando = True
        self.posicao_tab = 0
        self.valor_inicial = valor_inicial

    def subtrai_valor(self, valor_montante):
        self.valor_total -= valor_montante
    
    def proprietario_tem_quantia(self, valor_nesce):
        if self.valor_total >= valor_nesce:
            return True
        return False

    def remover_jogador(self):
        if self.valor_total <= 0:
            self.jogando = False
        return self.jogando

    def andar(self):
        jogar_dados = random.choice(range(1,7))
        self.posicao_tab += jogar_dados
        if self.posicao_tab > 19:
            print(self.nome, ' COMPLETOU UMA RODADA RECEBA 100,00 R$')
            self.valor_total += 100
            self.posicao_tab -= 19

        return self.posicao_tab
