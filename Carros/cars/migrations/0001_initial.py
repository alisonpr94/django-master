# Generated by Django 4.2.4 on 2023-08-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('factory_year', models.IntegerField(blank=True, null=True)),
                ('model_year', models.IntegerField(blank=True, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
