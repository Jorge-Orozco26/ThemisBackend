# Generated by Django 4.2.5 on 2023-10-31 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tramitesLeg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedimientos_legales',
            name='Fecha_Registro',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
