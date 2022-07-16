from rest_framework import serializers
from core.models import Tags


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'id')
        model = Tags
        read_only_fields = ('id',)
