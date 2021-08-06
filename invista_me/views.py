from django.http import request, response
from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoFrom
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Sum


@login_required(login_url='/login/')
def pagina(request):
    dados = {
        'dados': Investimento.objects.all()
    }

    return render(request, 'investimentos/pagina.html', context=dados)


@login_required(login_url='/login/')
def menu(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/menu.html', context=dados)


def some_view(request):
    dados = Investimento.objects.all()
    # dados = Investimento.objects.all()
    total = sum([dado.valor for dado in dados])
    # total = Investimento.objects.all().annotate(Sum('valor'))
    # valor_total = Investimento.objects.agregate(Sum('valor'))
    # total = Sum([valor for valor in dados])
    # total = sum([dado.valor for dado in dados])
    print(f"passou {dados}")
    print(f"total {total}")

    return render(request, 'investimentos/pagina.html', {'total': total})


def detalhe(request, id):
    dados = {
        'dados': Investimento.objects.get(pk=id)
    }
    return render(request, 'investimentos/detalhe.html', dados)


def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoFrom(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()  # salvando no banco de dados
        return redirect("pagina")  # redirecionando para pagina inicial
    else:
        investimento_form = InvestimentoFrom()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento_comum.html', context=formulario)


def editar(request, id):
    item = Investimento.objects.get(pk=id)
    if request.method == 'GET':
        formulario = InvestimentoFrom(instance=item)
        return render(request, 'investimentos/novo_investimento_comum.html', {'formulario': formulario})
    else:
        formulario = InvestimentoFrom(request.POST, instance=item)
        if formulario.is_valid():
            formulario.save()
        return redirect("pagina")


def excluir(request, id):
    item = Investimento.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('pagina')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': item})


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect("login")


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("menu")
        else:
            messages.error(
                request, "Usuario e senha Invalido. Tente novamente")
    return redirect("login")


# def investimento_registrado(request):
#     investimento = {
#         'tipo_investimento': request.POST.get('TipoInvestimento')
#     }
#     return render(request, 'investimentos/investimento_registrado.html', investimento)
