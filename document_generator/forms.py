from django import forms

class ItemForm(forms.Form):
    especificacao = forms.CharField(label="Especificação", max_length=255)
    catmat = forms.CharField(Label="CATMAT", max_Lenght=50)
    unidade_medida = forms.CharField(Label="Unidade de Medida", max_Lenght=50)
    quantidade = forms.CharField(Label="Quantidade")
    valor_unitario = forms.CharField(Label="Valor Unitário", max_digits=10, decimal_places=2)