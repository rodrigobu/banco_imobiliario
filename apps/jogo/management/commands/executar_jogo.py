import logging

from django.core.management.base import BaseCommand
from apps.jogo.models import Jogo

class Command(BaseCommand):
    ''' Executar os scripts do jogo via terminal
    '''

    def handle(self, *args, **options):
        jogo = Jogo()
        jogo.iniciar_jogo()
        for n in range(1, 301):
            jogo.iniciar_partida(n)
        jogo.save_historico()
