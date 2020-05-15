from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.jogo.models import Jogo
from api.serializers import JogoSerializer

class JogoViewSet(ModelViewSet):
    '''
    ModelViewSet que retornar todas as simulações executadas.
    '''
    http_method_names = ['get']
    serializer_class = JogoSerializer
    queryset = Jogo.objects.all()

class ExecutarJogoViewSet(ModelViewSet):
    '''
    ModelViewSet executa a simulação e retorna a simulação realizada
    '''
    http_method_names = ['get']
    serializer_class = JogoSerializer
    queryset = Jogo.objects.all()

    def list(self, request, *args, **kwargs):
        jogo = Jogo()
        jogo.iniciar_jogo()
        for n in range(1, 301):
            jogo.iniciar_partida(n)
        jogo.save_historico()

        queryset = self.queryset.latest()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)