# Generated by Django 2.0.3 on 2018-03-09 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='code ',
            new_name='code',
        ),
    ]
