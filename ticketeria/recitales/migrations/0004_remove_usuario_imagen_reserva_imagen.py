# Generated by Django 5.0.3 on 2024-03-15 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recitales', '0003_usuario_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='imagen',
        ),
        migrations.AddField(
            model_name='reserva',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
