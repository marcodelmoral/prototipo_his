# Generated by Django 4.0.5 on 2022-06-15 05:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dengue', '0003_remove_vector_cve_diag_final'),
        ]

    operations = [
        migrations.RenameField(
            model_name='vector',
            old_name='loc',
            new_name='geometry',
            ),
        migrations.RenameField(
            model_name='vector',
            old_name='des_loc_res',
            new_name='localidad',
            ),
        migrations.RemoveField(
            model_name='vector',
            name='des_edo_res',
            ),
        migrations.RemoveField(
            model_name='vector',
            name='des_mpo_res',
            ),
        ]