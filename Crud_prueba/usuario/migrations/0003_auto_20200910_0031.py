# Generated by Django 3.1 on 2020-09-10 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20200909_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ciudad',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='pais',
            name='provincia',
        ),
        migrations.RemoveField(
            model_name='provincia',
            name='ciudad',
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.provincia'),
        ),
        migrations.AddField(
            model_name='provincia',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.pais'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.ciudad'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.CharField(max_length=10, verbose_name='Cedula:'),
        ),
    ]