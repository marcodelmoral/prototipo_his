# Generated by Django 4.0.5 on 2022-06-15 04:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dengue', '0002_initial'),
        ]

    operations = [
        migrations.RemoveField(
            model_name='vector',
            name='cve_diag_final',
            ),
        ]
