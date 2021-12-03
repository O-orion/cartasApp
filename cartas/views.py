from django.shortcuts import redirect, render, get_object_or_404
from .models import Carta

def index(request):
    cartas = Carta.objects.all() #recuperando todas as carta no banco de dados
    dados = {
        'cartas':cartas
    }
    return render(request,'index.html', dados)

def novaCarta(request):
    if (request.method == 'POST'):
        titulo = request.POST['titulo']
        tema = request.POST['tema']
        remetente = request.POST['remetente']
        destinatario = request.POST['destinatario']
        texto = request.POST['texto']
        carta = Carta.objects.create(titulo = titulo, tema= tema, remetente= remetente, destinatario = destinatario, texto = texto)
        carta.save()
        return redirect('index')
    else:
      return render(request, 'novaCarta.html')

def editar_carta(request, carta_id):
    carta = get_object_or_404(Carta, pk=carta_id)
    carta_a_editar = { 'carta': carta}
    return render(request,'editarCarta.html', carta_a_editar)

def atualizar_carta(request):
    if request.method == 'POST':
        carta_id = request.POST['carta_id']
        r = Carta.objects.get(pk=carta_id)
        r.titulo = request.POST['titulo']
        r.tema = request.POST['tema']
        r.remetente = request.POST['remetente']
        r.destinatario = request.POST['destinatario']
        r.texto = request.POST['texto']
        r.save()
        return redirect('index')

def abrir_carta(request, carta_id):
    carta = get_object_or_404(Carta, pk=carta_id)
    carta_a_exibir = {'carta': carta}
    return render(request, 'abrir_carta.html', carta_a_exibir)

