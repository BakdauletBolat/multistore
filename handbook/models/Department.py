from django.db import models
class Department(models.Model):

    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True,on_delete=models.CASCADE)
    status = models.IntegerField() 
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    
