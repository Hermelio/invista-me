from django.forms import ModelForm, fields
from .models import Investimento


class InvestimentoFrom(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'
