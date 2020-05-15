from rest_framework import serializers
from apps.jogo.models import Jogo

class JogoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Jogo
        fields = '__all__'

    def create(self):
        jogo = Jogo()
        jogo.iniciar_jogo()
        for n in range(1, 301):
            jogo.iniciar_partida(n)
        return jogo.save_historico()