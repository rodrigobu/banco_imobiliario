from django.urls import path, include
from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register(r'jogo', views.JogoViewSet, 'jogo')
router.register(r'simular', views.ExecutarJogoViewSet, 'simular')

urlpatterns = [
    path('', include(router.urls))
]
