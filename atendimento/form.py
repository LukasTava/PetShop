from django.forms import ModelForm
from .models import Atendimento, Responsavel, Pet


class AtendimentoForm(ModelForm):
    class Meta:
        model = Atendimento
        fields = ['tipo', 'responsavel', 'descricao', 'data', 'pet']


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['nome', 'dono', 'telefone', 'lagradouro', 'numero', 'bairro', 'cidade', 'estado']


class ResponsavelForm(ModelForm):
    class Meta:
        model = Responsavel
        fields = ['nome', 'telefone', 'lagradouro', 'numero', 'bairro', 'cidade', 'estado', 'tipo']
