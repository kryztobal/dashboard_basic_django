# Generated by Django 2.1.1 on 2018-10-16 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiarios',
            fields=[
                ('cedula', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombres', models.CharField(default='', max_length=255)),
                ('cargo', models.CharField(default='', max_length=255)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gerencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='beneficiarios',
            name='gerencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beneficiarios.Gerencia'),
        ),
    ]
