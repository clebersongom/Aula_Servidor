# Generated by Django 4.1 on 2022-09-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCadastra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastroop',
            name='comprimento_capa',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cadastroop',
            name='expessura_capa',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cadastroop',
            name='hora_fim_prod',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cadastroop',
            name='hora_inicio_prod',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cadastroop',
            name='largura_capa',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cadastroop',
            name='quantidade_producao',
            field=models.CharField(max_length=20),
        ),
    ]
