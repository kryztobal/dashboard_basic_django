# Generated by Django 2.1.1 on 2018-10-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operativos', '0002_auto_20181018_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='operativo',
            name='proveedor',
            field=models.CharField(default='', max_length=255),
        ),
    ]
