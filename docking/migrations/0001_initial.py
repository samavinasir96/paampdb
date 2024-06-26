# Generated by Django 5.0.6 on 2024-06-12 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AMP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amp_no', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('sequence', models.TextField()),
                ('source', models.CharField(max_length=255)),
                ('tiny_number', models.IntegerField()),
                ('small_number', models.IntegerField()),
                ('aliphatic_number', models.IntegerField()),
                ('aromatic_number', models.IntegerField()),
                ('nonpolar_number', models.IntegerField()),
                ('polar_number', models.IntegerField()),
                ('charged_number', models.IntegerField()),
                ('basic_number', models.IntegerField()),
                ('acidic_number', models.IntegerField()),
                ('tiny_mole', models.FloatField()),
                ('small_mole', models.FloatField()),
                ('aliphatic_mole', models.FloatField()),
                ('aromatic_mole', models.FloatField()),
                ('nonpolar_mole', models.FloatField()),
                ('polar_mole', models.FloatField()),
                ('charged_mole', models.FloatField()),
                ('basic_mole', models.FloatField()),
                ('acidic_mole', models.FloatField()),
                ('molecular_weight', models.CharField(max_length=50)),
                ('length', models.IntegerField()),
                ('isoelectric_point', models.CharField(max_length=50)),
                ('aliphatic_index', models.FloatField()),
                ('antigenic', models.CharField(max_length=255)),
                ('toxicity', models.CharField(max_length=255)),
                ('cpp', models.CharField(max_length=255)),
                ('charge', models.CharField(max_length=50)),
                ('instability_index', models.CharField(max_length=50)),
                ('hydrophobicity', models.CharField(max_length=50)),
                ('hydrophobic_moment', models.CharField(max_length=50)),
                ('boman_index', models.CharField(max_length=50)),
                ('hp', models.CharField(max_length=50)),
                ('antimicrobial', models.CharField(max_length=255)),
                ('half_life', models.CharField(max_length=255)),
                ('pdb_name', models.CharField(max_length=1000, verbose_name='PDBName')),
                ('pdb_file', models.FileField(blank=True, null=True, upload_to='amp_pdb_files/')),
            ],
        ),
        migrations.CreateModel(
            name='PDBDQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PDBQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PDBTQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TargetProtein',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_protein', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dock', models.CharField(max_length=255)),
                ('pdb_structure', models.FileField(blank=True, null=True, upload_to='dock_pdb_files/')),
                ('pdb_structure_name', models.CharField(max_length=1000)),
                ('avg_rmsd', models.CharField(max_length=50)),
                ('lowest_rmsd', models.CharField(max_length=50)),
                ('binding_energy', models.CharField(max_length=50)),
                ('ligplot', models.CharField(max_length=50)),
                ('amp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docking.amp')),
                ('target_protein', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docking.targetprotein')),
            ],
        ),
        migrations.AddField(
            model_name='amp',
            name='target_protein',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='docking.targetprotein'),
        ),
    ]
