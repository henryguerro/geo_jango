from django.db import models


class Country(models.Model):
    CODE_CHOICES = (
        ('Colombia', 'co'),
        ('Argentina', 'ar'),
        ('Venezuela', 've')
    )

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, choices=CODE_CHOICES)
    continent = models.ForeignKey('continents.Continent', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
