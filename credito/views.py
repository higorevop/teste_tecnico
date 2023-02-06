from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from credito.models import Credito
from credito.serializers import CreditoSerializer


class CreditoView(ModelViewSet):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer

    @action(methods=['post'], detail=False)
    def calcular(self, request):
        credito_serializer = CreditoSerializer(data=request.data)
        if not credito_serializer.is_valid():
            return Response(credito_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        cpf = credito_serializer.validated_data.get('cpf')
        credito = Credito.objects.filter(cpf=cpf).last()
        if credito:
            return Response(CreditoSerializer(credito).data)

        credito = credito_serializer.save()
        juros = {1: 0.8, 5: 1.2, 10: 1.4, 15: 2.2, 20: 2.6, 25: 3.1}[credito.dia_pagamento]
        valor_total = credito.valor_solicitado * pow((1 + juros/100), credito.meses_parcelamento)
        credito.valor_parcelas = valor_total / credito.meses_parcelamento
        credito.renda_necessaria = valor_total * 0.1
        credito.juros = juros
        credito.valor_total = valor_total
        credito.save()

        return Response(CreditoSerializer(credito).data)
