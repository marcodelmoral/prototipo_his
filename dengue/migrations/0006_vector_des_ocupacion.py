# Generated by Django 4.0.5 on 2022-06-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dengue', '0005_vector_fol_id'),
        ]

    operations = [
        migrations.AddField(
            model_name='vector',
            name='des_ocupacion',
            field=models.CharField(blank=True, max_length=255, null=True),
            ),
        ]
