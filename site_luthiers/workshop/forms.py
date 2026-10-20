from django import forms
from .models import Luthier, Guitar

class LuthierForm(forms.ModelForm):
    class Meta:
        model = Luthier
        fields = ['nome', 'cidade', 'fundada_em', 'foto']

class GuitarForm(forms.ModelForm):
    class Meta:
        model = Guitar
        fields = ['modelo', 'ano', 'descricao', 'luthier', 'imagem']