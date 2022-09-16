# Generated by Django 4.1.1 on 2022-09-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveSmallIntegerField()),
                ('qualification', models.CharField(max_length=500)),
                ('gender', models.BooleanField()),
            ],
        ),
    ]