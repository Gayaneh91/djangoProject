import datetime
from django.db import models
from django.contrib.auth.models import User


class AcUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    registration_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.user.username}'