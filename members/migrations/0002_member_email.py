# Generated by Django 4.2.3 on 2023-07-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
    ]
