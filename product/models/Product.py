from django.db import models


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
    brand = models.ForeignKey('handbook.Brand',on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=255,null=True, blank=True)
    category = models.ForeignKey('handbook.Category',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Product(models.Model):
    base = models.OneToOneField(ProductBase,on_delete=models.DO_NOTHING,related_name='product')
    stores = models.ManyToManyField('store.Store',blank=True)
    cities = models.ManyToManyField('handbook.City')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.base.full_name
        
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

            
class ProductImage(models.Model):
    photo = models.ImageField(upload_to='product-images/')
    product_page = models.ForeignKey(Product,on_delete=models.CASCADE)