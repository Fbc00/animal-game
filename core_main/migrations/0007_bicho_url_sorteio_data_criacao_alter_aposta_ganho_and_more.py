# Generated by Django 4.0.6 on 2022-07-20 16:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core_main', '0006_remove_sorteio_hora_sorteio_data_sorteio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicho',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sorteio',
            name='data_criacao',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aposta',
            name='ganho',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='sorteio',
            name='bicho_sorteado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bicho_do_dia', to='core_main.bicho'),
        ),
        migrations.AlterField(
            model_name='sorteio',
            name='data_sorteio',
            field=models.DateField(null=True, unique=True),
        ),
    ]