# Generated by Django 3.1.5 on 2021-01-27 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos',
            old_name='nomero',
            new_name='numero',
        ),
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='La dirección'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
