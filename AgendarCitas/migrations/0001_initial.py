# Generated by Django 4.2.5 on 2023-11-14 15:49

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
            name='AgendarCita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_Cita', models.DateTimeField()),
                ('Nombre_Usuario_citado', models.CharField(max_length=255)),
                ('Descripcion', models.TextField()),
                ('Observacion', models.TextField()),
                ('usuario_agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]