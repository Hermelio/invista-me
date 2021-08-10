from django.urls import path
from . import views


app_name='usuario'

urlpatterns = [

	path('cadastro', views.cadastro, name='cadastro'),
]