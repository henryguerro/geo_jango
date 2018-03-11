from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    nationality = models.ManyToManyField('countries.Country', related_name='persons')
    father = models.OneToOneField('self', on_delete=models.CASCADE, null=True)