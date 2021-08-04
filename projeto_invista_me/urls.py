"""projeto_invista_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from projeto_invista_me.invista_me.views import pagina_inicial
from django.contrib import admin
from django.urls import path
from invista_me import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.pagina_inicial),
    path('novo_investimento/', views.criar, name='novo_investimento_comum'),
    path('novo_investimento/<int:id>', views.editar, name='editar'),
    path('excluir_investimento/<int:id>', views.excluir, name='excluir'),
    path('menu/', views.pagina,
         name='pagina'),
    path('', views.menu,
         name='menu'),
    path('<int:id>', views.detalhe,
         name='detalhe'),
]
