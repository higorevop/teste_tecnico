from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from credito.views import CreditoView


class CreditoViewTest(TestCase):

    @patch.object(CreditoView, '_simulacao_juros', return_value=1.2)
    def test_view_credito_calcular(self, mock):
        api = APIClient()
        data = {
            "valor_solicitado": "500",
            "meses_parcelamento": "12",
            "dia_pagamento": "5",
            "cpf": "111.000.111-00",
            "nome": "Usuário Comum"
        }
        response = api.post('/api/credito/calcular/', data, format='json')
        self.assertEqual(response.json().get('valor_parcelas'), 48.07894267427442)
        self.assertEqual(response.json().get('juros'), 1.2)
        self.assertEqual(response.json().get('renda_necessaria'), 57.69473120912931)
        self.assertEqual(response.json().get('valor_total'), 576.947312091293)
