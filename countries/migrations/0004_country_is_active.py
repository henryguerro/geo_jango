# Generated by Django 2.0.3 on 2018-03-11 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_country_continent'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]