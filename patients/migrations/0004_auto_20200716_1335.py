# Generated by Django 2.2 on 2020-07-16 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20200716_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienttable',
            name='DOB',
            field=models.DateField(max_length=250),
        ),
    ]
