# Generated by Django 2.1.1 on 2018-10-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operativos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operativo',
            name='nbolsas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operativo',
            name='nbolsasForaneas',
            field=models.IntegerField(default=0),
        ),
    ]
