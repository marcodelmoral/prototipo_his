# Generated by Django 3.2.13 on 2022-07-03 02:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dengue', '0012_auto_20220621_0330'),
        ]

    operations = [
        migrations.AddField(
            model_name='vector',
            name='ide_fec_nac',
            field=models.DateField(blank=True, null=True),
            ),
        ]
