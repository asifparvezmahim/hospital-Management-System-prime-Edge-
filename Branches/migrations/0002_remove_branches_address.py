# Generated by Django 5.1.3 on 2024-12-09 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Branches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branches',
            name='address',
        ),
    ]
