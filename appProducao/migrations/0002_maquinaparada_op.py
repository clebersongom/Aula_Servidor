# Generated by Django 4.1 on 2022-09-24 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appProducao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maquinaparada',
            name='op',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
