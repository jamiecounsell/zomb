from __future__ import unicode_literals
from django.db import models
import datetime

class Zombie(models.Model):

    DATE_OF_OUTBREAK = datetime.date(2016, 1, 1)

    name = models.CharField(max_length=100, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    date_of_rebirth = models.DateField(blank=False, null=False, default=DATE_OF_OUTBREAK)

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    bio = models.TextField()

