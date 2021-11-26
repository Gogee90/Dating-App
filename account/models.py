from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    avatar = models.ImageField(verbose_name='Avatar', upload_to='media', blank=True)
    gender = models.CharField(max_length=50, choices=gender_choices, blank=True)

    def __str__(self):
        return f'{self.username} {self.email}'
