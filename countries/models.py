from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Country(models.Model):
    CODE_CHOICES = (
        ('CO', 'colombia'),
        ('AR', 'argentina'),
        ('USA', 'Estados Unidos')
    )

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, choices=CODE_CHOICES)
    continent = models.ForeignKey('continents.Continent', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    is_active = ActiveManager()
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}[{self.pk}]'
