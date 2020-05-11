# -*- Coding: UTF-8 -*-
from tabuleiro import Tabuleiro

class Jogo():

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.tabuleiro.organizando_tabuleiro()
        self.turno = 0
        self.lista_turno = list()
        self.lista_vencedor = list()
        
    def jogadas_tab(self, jogadores, propriedades):
        ''' Metodo que simula as jogadas no tabuleiro.
        '''
        j1, j2, j3, j4 = jogadores
        j1.andar()
        j1.oportunidade_compra(propriedades[j1.posicao_tab])
        j2.andar()
        j2.oportunidade_compra(propriedades[j2.posicao_tab])
        j3.andar()
        j3.oportunidade_compra(propriedades[j3.posicao_tab])
        j4.andar()
        j4.oportunidade_compra(propriedades[j4.posicao_tab])
        
    def media_turno(self):
        ''' Metodo utilizado para fazer o calculo da media de turno.
        '''
        media = round(sum(self.lista_turno)/len(self.lista_turno))
        texto = '''
        Media de turno por partida: {}
            '''.format(media)
        return texto
            
    def vitorias_comportamento(self):
        ''' Metodo que capta a quantidade de vezes que cada comportamento
        venceu.
        '''
        cauteloso = self.lista_vencedor.count('Cauteloso')
        impulsivo = self.lista_vencedor.count('Impulsivo')
        aleatorio = self.lista_vencedor.count('Aleatorio')
        exigente = self.lista_vencedor.count('Exigente')
        return cauteloso, impulsivo, aleatorio, exigente
    
    def comportamente_vencedor(self):
        ''' Metodo que faz comparativo entre os quantro comportamentos
        e verifica que obteve o maior numero de vitoria
        '''
        cau, ale, imp, exi = self.vitorias_comportamento()
        texto = '''
        Comportamento vencedor: '''
        if (cau > ale and cau > imp and cau > exi):
            return texto + 'Cauteloso\n'
        elif (ale > cau and ale > imp and ale > exi):
            return texto + 'Aleatorio\n'
        elif (imp > cau and imp > ale and imp > exi):
            return texto + 'Impulsivo\n'
        else:
            return texto + 'Exigente\n'

    def percentual_comportamento(self):
        ''' Metodo utilizado para realizar o calculo do percentual
        de cada comportamento e formantando a saida do resultado.
        '''
        total = sum(self.vitorias_comportamento())
        cau, ale, imp, exi = self.vitorias_comportamento()

        per_cau = round(cau/(total/100), ndigits=2) 
        per_ale = round(ale/(total/100), ndigits=2)
        per_imp = round(imp/(total/100), ndigits=2)
        per_exi = round(exi/(total/100), ndigits=2)
        resposta = '''
        Porcentagem de Vitorias por comportamento: \n
        Aleatorio: {per_ale}%, \n
        Cauteloso: {per_cau}%, \n
        Exigente: {per_exi}%, \n
        Impulsivo: {per_imp}%
        '''.format(
                per_ale=per_ale,
                per_cau=per_cau,
                per_exi=per_exi,
                per_imp=per_imp
            )
        return resposta
        
    def iniciar_partida(self):
        ''' Metodo que inicia a partida.
        '''
        propriedades = self.tabuleiro.propriedades[0]
        jogadores = self.tabuleiro.jogadores
        self.turno = 0 
        for n in range(0,1000):
            self.turno += 1
            self.jogadas_tab(jogadores, propriedades)
            self.tabuleiro.devolver_propriedades_jogador()

            if len(self.tabuleiro.jogadores_ativo()) == 1:
                self.lista_turno.append(self.turno)
                self.lista_vencedor.append(self.tabuleiro.jogadores_ativo()[0].nome)
                break

        self.tabuleiro.novo_tabuleiro()
        
jogo = Jogo()
for n in range(1, 301):
    jogo.iniciar_partida()

print('Total de simulações: {}'.format(n))
print(jogo.media_turno())
print(jogo.percentual_comportamento())
print(jogo.comportamente_vencedor())

