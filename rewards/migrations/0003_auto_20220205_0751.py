# Generated by Django 3.1.7 on 2022-02-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0002_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewards',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]