# forms.py
from django import forms
from .models import Pasta

class PastaForm(forms.ModelForm):
    class Meta:
        model = Pasta
        fields = ['caminho']
