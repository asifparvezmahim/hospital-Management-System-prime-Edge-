# Generated by Django 5.1.3 on 2024-12-08 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departments',
            name='image',
        ),
    ]
