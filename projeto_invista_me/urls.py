from os import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
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
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('login/submit', views.submit_login),
]
