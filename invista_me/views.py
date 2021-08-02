from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoFrom


def pagina(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/pagina.html', context=dados)


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
        return render(request, 'investimentos/novo_investimentos.html', context=formulario)


def editar(request, id):
    item = Investimento.objects.get(pk=id)
    if request.method == 'GET':
        formulario = InvestimentoFrom(instance=item)
        return render(request, 'investimentos/novo_investimentos.html', {'formulario': formulario})
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

# def investimento_registrado(request):
#     investimento = {
#         'tipo_investimento': request.POST.get('TipoInvestimento')
#     }
#     return render(request, 'investimentos/investimento_registrado.html', investimento)
