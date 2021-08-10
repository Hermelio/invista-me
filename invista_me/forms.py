from django import forms
from django.forms import ModelForm, fields
from .models import Investimento
from django.forms import ModelForm, Textarea
from . import models


class InvestimentoFrom(ModelForm):
    class Meta:
        model = Investimento
        exclude = ['usuario']


# class ContactForm(ModelForm):
#     class Meta:
#         model = Contato
#         exclude = ['usuario']
    # nome_completo = forms.CharField(
    #     error_messages={'required': 'Obrigatório o preenchimento do nome'},
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Seu nome completo"
    #         }
    #     )
    # )
    # email = forms.EmailField(
    #     error_messages={'invalid': 'Digite um email válido!'},
    #     widget=forms.EmailInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Digite seu email"
    #         }
    #     )
    # )
    # mensagem = forms.CharField(
    #     error_messages={
    #         'required': 'É obrigatório o preenchimento do campo mensagem!'},
    #     widget=forms.Textarea(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Digite sua mensagem"
    #         }
    #     )
    # )

class QuestionForm(ModelForm):
    class Meta:
        model = models.Questions
        fields = ["nome_contato", "contact_email", "question"]
        # widgets = {
        #     "question": Textarea(attrs={"cols": 40, "rows": 20}),
        # }
