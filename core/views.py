from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    return render (request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')
    
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário/senha inválidos")
    return redirect('/')

@login_required(login_url='/login/')#Quando não logado, ele direcionada para login/
def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')#Quando não logado, ele direcionada para login/
def eventos(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'eventos.html', dados)

@login_required(login_url='/login/')#Quando não logado, ele direcionada para login/
def submit_eventos(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            Evento.objects.filter(id=id_evento).update(
                titulo=titulo,
                data_evento=data_evento,
                descricao=descricao
            )
        else:
            Evento.objects.create(
                titulo=titulo,
                data_evento=data_evento,
                descricao=descricao,
                usuario=usuario
            )
    return redirect('/')

@login_required(login_url='/login/')#Quando não logado, ele direcionada para login/
def delete_eventos(request, id_evento):
    Evento.objects.filter(id=id_evento).delete()
    return redirect('/')