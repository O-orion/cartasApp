from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('novaCarta', views.novaCarta, name="novaCarta"),
    path('editar/<int:carta_id>',views.editar_carta, name="editar_carta"),
    path('atualizar_carta', views.atualizar_carta, name="atualizar_carta"),
    path('abrir/<int:carta_id>', views.abrir_carta, name='abrir_carta'),
    path('deletar/<int:carta_id>', views.deletar_carta, name="deletar_carta")

]