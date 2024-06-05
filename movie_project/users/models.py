from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,null=True)
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True, verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True, verbose_name='user permissions', help_text='Specific permissions for this user.')

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'



# Create your models here.
