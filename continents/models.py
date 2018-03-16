from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    color = models.CharField(max_length=255)


    def __str__(self):
        return self.name
