from django.test import TestCase
from django.test import Client


class ApiJogoTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.get('/executar/')

    def test_api_jogo_simulacao(self):
        ''' Teste para verificar se a simulação via api esta faz executando de maneira
        correta e retornando o json da ultima simulação
        '''
        response = self.client.get('/executar/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())

    def test_api_jogo_lista(self):
        ''' Teste para verificar se API está trazendo todas as simulações executadas
        '''
        response = self.client.get('/jogo/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
