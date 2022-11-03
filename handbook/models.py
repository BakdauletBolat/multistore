from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='lang-images/')
    uid = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Язык'


class Brand(models.Model):
    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255)
    status = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name = 'Качество'
        verbose_name_plural = 'Качествы'


class Category(models.Model):
    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255)
    status = models.BooleanField()
    stores = models.ManyToManyField('store.Store',related_name='categories')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='categories')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'


class City(models.Model):
    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Department(models.Model):
    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    status = models.IntegerField()
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Quality(models.Model):
    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255)
    status = models.BooleanField()
    alias = models.CharField(max_length=255)
    order = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name = 'Качество'
        verbose_name_plural = 'Качествы'


class WareHouse(models.Model):
    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255)
    status = models.BooleanField()
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE, null=True, blank=True, related_name='warehouses')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, related_name='warehouses')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
