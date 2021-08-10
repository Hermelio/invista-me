from django.urls import path
from django.urls.conf import include
from invista_me import views


app_name = 'invista'

urlpatterns = [

    path("/troca-senha", views.teste01, name='teste'),
    path("/contato", views.contato, name='contato'),
]
