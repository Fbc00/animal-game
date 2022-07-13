# Generated by Django 4.0.6 on 2022-07-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_main', '0002_aposta_ganho_aposta_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=16)),
                ('sobrenome', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=128)),
                ('usuario', models.CharField(max_length=32)),
                ('senha', models.CharField(max_length=32)),
            ],
        ),
    ]
