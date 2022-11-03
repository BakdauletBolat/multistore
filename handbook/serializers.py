from rest_framework import serializers
from handbook.models import Category, City, WareHouse


class CategoryBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(method_name='get_children')

    class Meta:
        model = Category
        fields = ('id', 'name', 'children')

    @staticmethod
    def get_children(obj):
        if len(obj.categories.filter(stores__in=[1])) >= 1:
            return CategorySerializer(obj.categories.filter(stores__in=[1]), many=True).data
        else:
            return []


class CategoryWithParentSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField(method_name='get_parent')

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')

    @staticmethod
    def get_parent(obj):
        if obj.parent is not None:
            return CategoryWithParentSerializer(obj.parent).data
        else:
            return None


class WareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouse
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'uid', 'name')
