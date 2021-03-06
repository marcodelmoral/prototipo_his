# Generated by Django 4.0.5 on 2022-06-15 03:00

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ]

    operations = [
        migrations.CreateModel(
            name='Vector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('ide_nom', models.CharField(blank=True, max_length=255, null=True)),
                ('ide_ape_pat', models.CharField(blank=True, max_length=255, null=True)),
                ('ide_ape_mat', models.CharField(blank=True, max_length=255, null=True)),
                ('ide_sex',
                 models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Masculino'), (2, 'Femenino')], null=True)),
                ('num_ext', models.CharField(max_length=255)),
                ('num_int', models.CharField(blank=True, max_length=255, null=True)),
                ('ide_cal', models.CharField(max_length=255)),
                ('ide_cp', models.CharField(max_length=5)),
                ('ide_col', models.CharField(blank=True, max_length=255, null=True)),
                ('cve_diag_final', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'DENGUE NO GRAVE'), (
                    10, 'DENGUE CON SIGNOS DE ALARMA - ENFERMEDAD POR VIRUS ZIKA'), (3, 'DENGUE GRAVE'), (8,
                                                                                                          'ENFERMEDAD POR VIRUS ZIKA'),
                                                                                         (6,
                                                                                          'DENGUE CON SIGNOS DE ALARMA - FIEBRE CHIKUNGUNYA'),
                                                                                         (2,
                                                                                          'DENGUE CON SIGNOS DE ALARMA'),
                                                                                         (5,
                                                                                          'DENGUE NO GRAVE - FIEBRE CHIKUNGUNYA')],
                                                                    null=True)),
                ('precision', models.BooleanField(default=False)),
                ('des_diag_final', models.CharField(blank=True, max_length=255, null=True)),
                ('loc', django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326)),
                ('fec_sol_aten', models.DateField(blank=True, null=True)),
                ],
            ),
        ]
