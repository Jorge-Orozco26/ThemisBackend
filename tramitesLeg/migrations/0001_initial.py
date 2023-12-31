# Generated by Django 4.2.5 on 2023-10-21 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plantilla_Solicitud',
            fields=[
                ('ID_Plantilla_Solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.TextField()),
                ('Contenido', models.TextField()),
                ('ID_Procedimiento_Legales', models.IntegerField()),
                ('Usuario_Registro', models.CharField(max_length=50)),
                ('Fecha_Registro', models.DateTimeField()),
                ('Estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Procedimientos_Legales',
            fields=[
                ('ID_Procedimientos_Legales', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_Procedimiento', models.CharField(max_length=255)),
                ('DescripcionProcedimiento', models.TextField()),
                ('PasosSeguir', models.TextField()),
                ('Usuario_Registro', models.CharField(max_length=50)),
                ('Fecha_Registro', models.DateTimeField()),
                ('Estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitudes_Rellenas',
            fields=[
                ('ID_Solicitudes_Rellenas', models.AutoField(primary_key=True, serialize=False)),
                ('ID_Usuario', models.IntegerField()),
                ('ID_Plantilla_Solicitud', models.IntegerField()),
                ('Contenido_Rellenado', models.TextField()),
                ('Usuario_Registro', models.CharField(max_length=50)),
                ('Fecha_Registro', models.DateTimeField()),
                ('Estado', models.BooleanField()),
                ('plantilla_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tramitesLeg.plantilla_solicitud')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='plantilla_solicitud',
            name='procedimiento_legales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tramitesLeg.procedimientos_legales'),
        ),
        migrations.AddField(
            model_name='plantilla_solicitud',
            name='usuario_creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
