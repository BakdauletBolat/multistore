from django.db import models
from handbook.models import Quality

class PriceType(models.Model):
    uid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    status = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип Цен'
        verbose_name_plural = 'Типы Цен'


class ProductBase(models.Model):
    uid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    status = models.BooleanField()
    brand = models.ForeignKey('handbook.Brand', on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey('handbook.Category', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Product(models.Model):
    base = models.OneToOneField(ProductBase, on_delete=models.DO_NOTHING, related_name='product')
    stores = models.ManyToManyField('store.Store', blank=True)
    cities = models.ManyToManyField('handbook.City')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.base.full_name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    photo = models.ImageField(upload_to='product-images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class ProductPage(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    lang = models.ForeignKey('handbook.Language', null=True, blank=True, on_delete=models.CASCADE)
    city = models.ForeignKey('handbook.City', null=True, blank=True, on_delete=models.CASCADE)
    store = models.ForeignKey('store.Store', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('lang', 'store', 'product', 'city')

    def __str__(self):
        return f'{self.id}: {self.title}'


class Price(models.Model):
    product = models.ForeignKey(ProductBase, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='prices')
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='prices')
    price_type = models.ForeignKey(PriceType, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='prices')
    cost = models.BigIntegerField()
    updated_at = models.DateTimeField(null=True, blank=True)
    uid = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.product is None:
            return f'Товар удален - {self.cost}'
        else:
            return f"{self.product.full_name} - {self.cost} тг"

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
