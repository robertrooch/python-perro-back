# Generated by Django 3.1.3 on 2024-05-13 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True)),
                ('raza', models.TextField(blank=True)),
                ('edad', models.IntegerField()),
                ('foto', models.URLField(blank=True)),
            ],
        ),
    ]
