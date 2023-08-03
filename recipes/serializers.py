from rest_framework import serializers
from .models import Tag, Recipe


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'author', 'category',
            'public', 'preparation', 'author', 'tags',
            'tags_objects', 'tags_links',
        ]
    public = serializers.BooleanField(
        source='is_published',
        read_only=True
    )
    preparation = serializers.SerializerMethodField(
        method_name='any_method_name',
        read_only=True
    )
    category = serializers.StringRelatedField(
        read_only=True
    )
    tags_objects = TagSerializer(
        many=True,
        source='tags',
        read_only=True
    )
    tag_links = serializers.HyperlinkedRelatedField(
        many=True,
        source='tags',
        view_name='recipes:recipe_api_v2_tag',
        read_only=True
    )

    def any_method_name(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
