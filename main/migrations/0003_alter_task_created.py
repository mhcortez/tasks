# Generated by Django 5.1.2 on 2024-10-30 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
