# Generated by Django 4.1 on 2022-09-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProducao', '0012_alter_maquinaparada_data_parada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinaparada',
            name='data_parada',
            field=models.DateTimeField(default='1000-01-01 00:00:00.000000'),
        ),
        migrations.AlterField(
            model_name='maquinaparada',
            name='data_retorno',
            field=models.DateTimeField(default='1000-01-01 00:00:00.000000'),
        ),
    ]
