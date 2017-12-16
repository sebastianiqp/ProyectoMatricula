from rest_framework.serializers import ModelSerializer
from Categoria.models import Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        # fields = ('cod_categoria')
        fields = '__all__'
