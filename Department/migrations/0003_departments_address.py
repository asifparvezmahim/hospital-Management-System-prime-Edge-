# Generated by Django 5.1.3 on 2024-12-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0002_remove_departments_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='address',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]