# Generated by Django 2.0.3 on 2018-03-10 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='nacionality',
            new_name='nationality',
        ),
        migrations.AddField(
            model_name='person',
            name='father',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Person'),
        ),
    ]