from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_publicacao': forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'editora': forms.Select(attrs={'class': 'form-control'}),
        }  

class FiltroForm(forms.Form):

    categoria = forms.CharField(required=False, label='Categoria')
    editora = forms.CharField(required=False, label='Editora')
    autor = forms.CharField(required=False, label='Autor')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['categoria'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoria'})
        
        self.fields['editora'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Editora'})
        
        self.fields['autor'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Autor'})

    
