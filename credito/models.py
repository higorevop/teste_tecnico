from django.db import models


class Credito(models.Model):
    cpf = models.CharField('CPF', max_length=18)
    nome = models.CharField('Nome', max_length=25)
    valor_solicitado = models.FloatField('Valor solicitado')
    meses_parcelamento = models.IntegerField('Meses parcelamento')
    dia_pagamento = models.IntegerField('Dia pagamento')
    valor_parcelas = models.FloatField('Valor da parcela', null=True, blank=True)
    juros = models.FloatField('Juros', null=True, blank=True)
    renda_necessaria = models.FloatField('Renda necessária', null=True, blank=True)
    valor_total = models.FloatField('Valor total', null=True, blank=True)
