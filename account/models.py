from django.contrib.auth.models import AbstractUser
from django.db import models
from geopy.distance import great_circle


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
        current_user_location = (self.latitude, self.longitude)
        for user in User.objects.all().exclude(id=self.id):
            return great_circle(current_user_location, (user.latitude, user.longitude)).km
