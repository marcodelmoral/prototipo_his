# Generated by Django 4.0.5 on 2022-06-15 03:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('geo', '0001_initial'),
        ]

    operations = [
        migrations.AlterField(
            model_name='localidad',
            name='cvegeo',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
            ),
        ]