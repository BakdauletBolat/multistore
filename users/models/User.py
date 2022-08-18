from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)


class UserManager(BaseUserManager):
    def create_user(self, email,phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone
        )

    

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,phone, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            phone=phone,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Почта',
        max_length=255,
        unique=True,
    )

    phone = models.CharField('Телефон',max_length=255,unique=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone'] 

    manager = UserManager()

    class Meta:
        app_label = 'users'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
