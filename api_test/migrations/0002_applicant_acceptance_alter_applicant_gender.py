# Generated by Django 4.1.1 on 2022-09-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='acceptance',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]