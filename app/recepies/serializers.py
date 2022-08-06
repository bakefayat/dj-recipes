from rest_framework import serializers
from core.models import Tags, Ingredients


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'id')
        model = Tags
        read_only_fields = ('id',)


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:        
        fields = ('name', 'id')
        model = Ingredients
        read_only_fields = ('id',)
