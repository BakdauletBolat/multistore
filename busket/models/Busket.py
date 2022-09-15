from django.db import models


class Busket(models.Model):

    uuid_user = models.UUIDField(null=True,blank=True)
    user = models.ForeignKey('users.User',null=True,blank=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        if self.user is not None:
            return str(self.user)
        return str(self.uuid_user)

    class Meta:

        verbose_name = "Корзина"