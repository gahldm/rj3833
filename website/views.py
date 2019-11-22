from django.shortcuts import render, redirect
from website.models import Cliente
from website.forms import FormCliente

def home(request):
    return render(request, 'website/index.html')

def cadastrarCliente (request):
    form = FormCliente(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    else:
        return render(request, 'website/cadastro.html', {'form':form, 'acao':'Atualizar'})

def listaCliente (request):
    dados = Cliente.objects.all()
    return render(request, 'website/listagem.html', {'dados': dados})
