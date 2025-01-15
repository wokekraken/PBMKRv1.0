from django.db import models

class Item(models.model):
    especificacao = models.CharField(max_lenght=255)
    catmat = models.CharField(max_lenght=50)
    unidade_medida = models.CharField(max_lenght=50)
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def valor_total(self):
        return self.quantidade * self.valor_unitario

