# Generated by Django 2.2 on 2020-07-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PATIENT_NAME', models.CharField(default='NULL', max_length=250)),
                ('EMAIL', models.CharField(default='NULL', max_length=250)),
                ('GENDER', models.CharField(default='NULL', max_length=250)),
                ('DOB', models.DateField(default='NULL', max_length=250)),
                ('CONTACT', models.CharField(default='NULL', max_length=20)),
            ],
        ),
    ]
