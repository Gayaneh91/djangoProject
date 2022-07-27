from django.db import models

from django.db import models
# Create your models here.

class Kino(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=30)
    original_name = models.PositiveSmallIntegerField(default=0)
    country = models.FloatField()

    def __str__(self):
        return self.name

# Create your models here.
