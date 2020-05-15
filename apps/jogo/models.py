from django.db import models
from apps.jogo.mixins.tabuleiro import Tabuleiro

class Jogo(models.Model):

    partidas = models.IntegerField()
    total_turnos = models.IntegerField()
    media_turnos = models.IntegerField()
    vencedor = models.CharField(max_length=50)
    timeout = models.IntegerField()
    aleatorio = models.FloatField()
    cauteloso = models.FloatField()
    exigente = models.FloatField()
    impulsivo = models.FloatField()

    class Meta:
        verbose_name = ("jogo")
        verbose_name_plural = ("jogos")
        get_latest_by = ['pk']


    def __str__(self):
        return str(self.pk)

    def iniciar_jogo(self):
        self.tabuleiro = Tabuleiro()
        self.tabuleiro.organizando_tabuleiro()
        self.timeout = 0 
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
        self.media_turnos = round(sum(self.lista_turno)/self.partidas)
        self.total_turnos = sum(self.lista_turno)
        texto = '''
        Media de turno por partida: {}
            '''.format(self.media_turnos)
        return texto
            
    def vitorias_comportamento(self):
        ''' Metodo que capta a quantidade de vezes que cada comportamento
        venceu.
        '''
        cauteloso = self.lista_vencedor.count('Cauteloso')
        impulsivo = self.lista_vencedor.count('Impulsivo')
        aleatorio = self.lista_vencedor.count('Aleatorio')
        exigente = self.lista_vencedor.count('Exigente')
        timeout = self.lista_vencedor.count('Time Out')
        return cauteloso, impulsivo, aleatorio, exigente, timeout
    
    def comportamente_vencedor(self):
        ''' Metodo que faz comparativo entre os quantro comportamentos
        e verifica que obteve o maior numero de vitoria
        '''
        cau, ale, imp, exi, tout = self.vitorias_comportamento()
        texto = '''
        Comportamento vencedor: '''
        if (cau > ale and cau > imp and cau > exi):
            self.vencedor = 'Cauteloso'
        elif (ale > cau and ale > imp and ale > exi):
            self.vencedor = 'Aleatorio'
        elif (imp > cau and imp > ale and imp > exi):
            self.vencedor = 'Impulsivo\n'
        else:
            self.vencedor = 'Exigente\n'
        return texto + self.vencedor

    def percentual_comportamento(self):
        ''' Metodo utilizado para realizar o calculo do percentual
        de cada comportamento e formantando a saida do resultado.
        '''
        cau, ale, imp, exi, tout = self.vitorias_comportamento()

        self.aleatorio = round(cau/(self.partidas/100), ndigits=2) 
        self.cauteloso = round(ale/(self.partidas/100), ndigits=2)
        self.exigente = round(imp/(self.partidas/100), ndigits=2)
        self.impulsivo = round(exi/(self.partidas/100), ndigits=2)
        per_tout = round(tout/(self.partidas/100), ndigits=2)

        self.media_vencedor = '''
        Aleatorio: {per_ale}%, \n
        Cauteloso: {per_cau}%, \n
        Exigente: {per_exi}%, \n
        Impulsivo: {per_imp}%\n
        Time Out: {per_tout}%
        '''.format(
                per_ale=self.aleatorio,
                per_cau=self.cauteloso,
                per_exi=self.exigente,
                per_imp=self.impulsivo, 
                per_tout=per_tout, 
            )
        
    def iniciar_partida(self, npartida):
        ''' Metodo que inicia a partida.
        '''
        propriedades = self.tabuleiro.propriedades[0]
        jogadores = self.tabuleiro.jogadores
        self.turno = 0 

        self.partidas = 0
        for n in range(0,1000):
            self.turno += 1
            self.jogadas_tab(jogadores, propriedades)
            self.tabuleiro.devolver_propriedades_jogador()

            if self.turno == 1000:
                self.timeout += 1
                self.lista_vencedor.append('Time Out')
                break
                        
            if len(self.tabuleiro.jogadores_ativo()) == 1:
                
                self.lista_vencedor.append(self.tabuleiro.jogadores_ativo()[0].nome)
                self.partidas += npartida
                break

        self.lista_turno.append(self.turno)
        self.tabuleiro.novo_tabuleiro()
        
    def resultado_simulacao(self):
        self.percentual_comportamento()
        
        texto = '''
        Total de Partidas: {partidas}\n
        Total de Turnos: {total_turnos}\n
        Média de Turno por Partida: {media_turnos}\n
        Partidas terminada em time out: {timeout}\n
        Comportamento Vencedor: {vencedor}
        {media_vencedor}
        '''.format(
            partidas=self.partidas,
            total_turnos=self.total_turnos,
            media_turnos=self.media_turnos,
            timeout=self.timeout,
            vencedor=self.vencedor,
            media_vencedor=self.media_vencedor
        )
        
        return texto

    def save_historico(self, resultado=False):
        self.media_turno()
        self.percentual_comportamento()
        self.comportamente_vencedor()
        if resultado:
            print(self.resultado_simulacao())

        self.save()
