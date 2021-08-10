from django.http import request, response
from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento, Questions
from .forms import InvestimentoFrom, QuestionForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Sum
from . import forms
from . import models


@login_required(login_url='/login/')
def pagina(request):

    dados = Investimento.objects.filter(usuario=request.user)
    total_pago = dados.filter(pago=True).aggregate(Sum('valor'))
    total_geral = dados.aggregate(Sum('valor'))
    contexto = {
        'dados': dados,
        'total': total_geral,
    }

    return render(request, 'investimentos/pagina.html', contexto)


@login_required(login_url='/login/')
def pagina_inicial(request):
    pagina = 'investimentos/pagina_inicial.html'
    dados = {
        'dados': Investimento.objects.all()
    }

    return render(request, pagina)


def contato(request):
    if request.method == "POST":
        form = forms.QuestionForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome_contato']
            email = form.cleaned_data['contact_email']
            questao = form.cleaned_data['question']
            salvando = Questions.objects.create(
                nome_contato=nome, contact_email=email, question=questao)
            salvando.save()
        # Redirecionando para pagina inicial
        return redirect('pagina_inicial')
    else:
        form = forms.QuestionForm()

    return render(request, 'investimentos/contato.html', {"form": form})


# def contato(request):
#     if request.method == 'POST':
#         contact_form = ContactForm(request.POST)
#         if contact_form.is_valid():
#             print(contact_form)
#             salvando = contact_form.save(commit=False)
#             salvando.save()
    #     form_email = contact_form.cleaned_data['email']
    #     print(form_email)
    #     form_name = contact_form.cleaned_data['nome_completo']
    #     print(form_name)
    #     form_question = contact_form.cleaned_data['mensagem']
    #     print(form_question)
    #     print(contact_form.cleaned_data)
    #     saving_all = Contato(
    #         nome_contato=form_name, email_contato=form_email, campo_contato=form_question)
    #     saving_all.save()
    # else:
    #     contact_form = forms.ContactForm()
    #     return redirect("pagina_inicial")
    # else:
    #     print('Erro ao salvar dados')
    # contexto = {'formulario': ContactForm()}
    # return render(request, 'investimentos/contato.html', contexto)


@login_required(login_url='/login/')
def menu(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/menu.html', context=dados)


def some_view(request):
    dados = Investimento.objects.all()
    total_geral = dados.agregate(Sum(dados.valor))
    total = sum([dado.valor for dado in dados])
    print(total_geral)
    print(f"passou {dados}")
    print(f"total {total}")
    contexto = {'dados': dados}
    return render(request, 'investimentos/pagina.html', contexto)


def detalhe(request, id):

    dados = Investimento.objects.get(pk=id)
    if dados.usuario != request.user:
        return redirect('novo_investimento_comum')
    dados = {
        'dados': dados
    }

    return render(request, 'investimentos/detalhe.html', dados)


def criar(request):

    if request.method == 'POST':
        investimento_form = InvestimentoFrom(request.POST)
        if investimento_form.is_valid():
            # salvando no banco de dados
            user = investimento_form.save(commit=False)
            user.usuario = request.user
            user.save()
        return redirect('pagina_inicial')  # redirecionando para pagina inicial
    else:
        print('Erro ao salvar dados')

    contexto = {'formulario': InvestimentoFrom()}
    return render(request, 'investimentos/novo_investimento_comum.html', contexto)


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
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("pagina_inicial")
        else:
            messages.error(
                request, "Usuario e senha Invalido. Tente novamente")
    return redirect("login")


# def investimento_registrado(request):
#     investimento = {
#         'tipo_investimento': request.POST.get('TipoInvestimento')
#     }
#     return render(request, 'investimentos/investimento_registrado.html', investimento)


def teste01(request):
    template_name = 'investimentos/teste.html'
    return render(request, template_name)
