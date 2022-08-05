from django.db import models

class Movies(models.Model):
    objects = None
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    view = models.IntegerField(default=0)
    about = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.author} - {self.view} - {self.about}'


class Songs(models.Model):
    objects = None
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    view = models.IntegerField(default=0)
    about = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.author} - {self.view} - {self.about}'

# Create your models here.
