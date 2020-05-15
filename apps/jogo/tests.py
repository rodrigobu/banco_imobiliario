from django.test import TestCase

from apps.jogo.models import Jogo
from apps.jogo.mixins.tabuleiro import Tabuleiro

class JogoTestCase(TestCase):

    def setUp(self):
        self.jogo = Jogo()
        self.tabuleiro = Tabuleiro()
        self.jogo.iniciar_jogo()
        for n in range(1,301):
            self.jogo.iniciar_partida(n)
        self.jogo.save_historico()


    def test_partidas_salvas(self):
        '''Teste para verificar se as partidas estão sendo salva.
        '''
        jogo = Jogo.objects.latest()
        self.assertTrue(jogo.partidas)
        
    def test_media_turno(self):
        '''Teste para verificar se as media do turno está sendo salva.
        '''
        jogo = Jogo.objects.latest()
        self.assertTrue(jogo.media_turnos)

    def test_total_turnos(self):
        '''Teste para verificar se as media do turno está sendo salva.
        '''
        jogo = Jogo.objects.latest()
        self.assertTrue(jogo.total_turnos)

    def test_vencedor(self):
        '''Teste para verificar se ha registro de vencedor.
        '''
        jogo = Jogo.objects.latest()
        self.assertTrue(jogo.vencedor)

    def test_timeout(self):
        '''Teste para verificar se tem partidas que sofreram timeout.
        '''
        jogo = Jogo.objects.latest()
        self.assertTrue(jogo.timeout)

    def test_media_vencedor(self):
        '''Teste para verificar se registros de cada comportamento.
        '''
        jogo = Jogo.objects.latest()
        self.assertTrue(jogo.aleatorio)
        self.assertTrue(jogo.cauteloso)
        self.assertTrue(jogo.exigente)
        self.assertTrue(jogo.impulsivo)

    def test_verificar_jogador(self):
        ''' Teste que verifica se todos os jogadores foram instanciado.
        '''
        self.tabuleiro.organizando_tabuleiro()
        jogadores = self.tabuleiro.jogadores
        self.assertEqual(len(jogadores), 4)

    def test_inativar_jogador(self):
        ''' Teste que verifica se o metodo de inativação se está funcionando com quando o montante
        do jogador chega a zero.
        '''
        self.tabuleiro.organizando_tabuleiro()
        jogador = self.tabuleiro.jogadores[0]
        jogador.subtrair_valor(jogador.valor_total)
        jogadores_ativos = self.tabuleiro.jogadores_ativo()
        self.assertFalse(jogador in jogadores_ativos)

    def test_jogador_andando(self):
        ''' Teste que verifica se o metodo de andar se está funcionando corretamente.
        '''
        self.tabuleiro.organizando_tabuleiro()
        jogador = self.tabuleiro.jogadores_ativo()[0]
        posicao_ini = jogador.posicao_tab
        jogador.andar()
        posicao_fin = jogador.posicao_tab
        self.assertTrue(posicao_ini < posicao_fin)

    def test_propriedades(self):
        ''' Teste que verifica se todas as propriedas foram adicionadas no tabuleiro.
        '''
        self.tabuleiro.organizando_tabuleiro()
        propriedades = self.tabuleiro.propriedades[0].keys()
        self.assertEqual(len(propriedades), 20)
