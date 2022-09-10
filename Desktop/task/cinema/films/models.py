from django.db import models
from datetime import date
# Create your models here.

class Film(models.Model):

    name = models.CharField(max_length=70)
    year = models.DateTimeField(default=date.today)
    rate = models.FloatField()
    number_of_users = models.FloatField(default=0)

    def __str__(self):
        return self.name


