from django.shortcuts import render, redirect
from invista_me.models import User
from django.contrib.auth import login, authenticate


def cadastro(request):
    users = User.objects.all()
    template_name = 'usuario/cadastro.html'
    if request.method == 'POST':
        user = request.POST['username']
        email = request.POST['email']
        senha = request.POST['password']
        if users.filter(username=user).exists() or users.filter(email=email).exists():
            print("email ou usuario ja cadastrado")
        else:
            if senha == request.POST['confirm_password']:

                new_user = User.objects.create_user(
                    username=user, email=email, first_name=user, password=senha)
                new_user.save()
                user_ = authenticate(request, username=user, password=senha)
                login(request, user_)
                return redirect('pagina_inicial')
            else:
                print("Senha nao confere")

    return render(request, template_name)
