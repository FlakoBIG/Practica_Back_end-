# Generated by Django 3.2 on 2024-10-22 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('Arma', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
