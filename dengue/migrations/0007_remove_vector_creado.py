# Generated by Django 4.0.5 on 2022-06-15 05:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dengue', '0006_vector_des_ocupacion'),
        ]

    operations = [
        migrations.RemoveField(
            model_name='vector',
            name='creado',
            ),
        ]
