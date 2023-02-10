from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField(
        read_only=True
    )
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(
        read_only=True
    )

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, category, validated_data):
        category.name = validated_data.get('name', category.name)
        category.kind = validated_data.get('kind', category.kind)
        category.save()
        return category
