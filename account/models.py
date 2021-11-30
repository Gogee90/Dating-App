from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from geopy.distance import great_circle
from .middleware import current_user
from .utils.create_watermarked_picture import create_watermarked_picture


class User(AbstractUser):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    avatar = models.ImageField(verbose_name='Avatar', upload_to='media', blank=True)
    gender = models.CharField(max_length=50, choices=gender_choices, blank=True)
    latitude = models.DecimalField(decimal_places=10, max_digits=20, verbose_name='Latitude', blank=True, null=True)
    longitude = models.DecimalField(decimal_places=10, max_digits=20, verbose_name='Longitude', blank=True, null=True)

    verbose_name = 'User'
    verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.username} {self.email}'

    @property
    def distance(self):
        request_user = current_user.get_current_user()
        if not request_user.is_anonymous:
            current_user_location = (request_user.latitude, request_user.longitude)
            return great_circle(current_user_location, (self.latitude, self.longitude)).km


@receiver(pre_save, sender=User)
def user_pre_save(instance, sender, **kwargs):
    if instance.avatar:
        instance.avatar = create_watermarked_picture(instance.avatar)
