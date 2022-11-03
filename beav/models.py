from django.db import models
from product.models import Product
from handbook.models import Category


class Value(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Поля'
        verbose_name_plural = 'Поля'


class Attribute(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Аттрибут'
        verbose_name_plural = 'Аттрибуты'


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Entity(models.Model):
    values = models.ManyToManyField(Value, related_name='entities')
    attribute = models.ForeignKey(Attribute, related_name='entities', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='entities', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='entities', on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, related_name='entities', on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.attribute}: in group: {self.group} - {self.values.values_list('name', flat=True)}"

    class Meta:
        verbose_name = 'Сущность'
        verbose_name_plural = 'Сущности'
