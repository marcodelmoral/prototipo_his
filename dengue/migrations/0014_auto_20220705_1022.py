# Generated by Django 3.2.13 on 2022-07-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dengue', '0013_vector_ide_fec_nac'),
        ]

    operations = [
        migrations.RemoveField(
            model_name='vector',
            name='des_diag_final',
            ),
        migrations.AddField(
            model_name='vector',
            name='cve_diag_final',
            field=models.PositiveSmallIntegerField(
                choices=[(1, 'Dengue no grave'), (3, 'Dengue grave'), (2, 'Dengue con signos de alarma')], null=True),
            ),
        ]
