from django.db import models


class Photo(models.Model):

    photo = models.ImageField(null=True,blank=True,upload_to='images/')
    name = models.CharField(null=True,blank=True,max_length=255)
