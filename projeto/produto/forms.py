from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = '__all__'
        
        widgets = {
			'importado': forms.TextInput(attrs={'class': 'form-check-input', }),
   
		}