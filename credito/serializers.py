from rest_framework.serializers import ModelSerializer

from credito.models import Credito


class CreditoSerializer(ModelSerializer):
    class Meta:
        model = Credito
        fields = '__all__'
