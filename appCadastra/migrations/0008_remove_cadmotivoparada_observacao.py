# Generated by Django 4.1 on 2022-10-06 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCadastra', '0007_cadmotivoparada_observacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadmotivoparada',
            name='observacao',
        ),
    ]
