# Generated by Django 4.1 on 2022-09-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProducao', '0011_alter_maquinaparada_data_parada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinaparada',
            name='data_parada',
            field=models.DateTimeField(default='0000-00-00 00:00:00.000000'),
        ),
        migrations.AlterField(
            model_name='maquinaparada',
            name='data_retorno',
            field=models.DateTimeField(default='0000-00-00 00:00:00.000000'),
        ),
    ]