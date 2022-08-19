from rest_framework import serializers
from handbook.models.Category import Category

class CategoryTransformer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(method_name='get_children')

    class Meta:
        model = Category
        fields = ('id', 'name', 'children',)

    def get_children(self, obj):
        if len(obj.categories.filter(store_id=1)) >= 1:
            return CategoryTransformer(obj.categories.filter(store_id=1),many=True).data
        else:
            return []