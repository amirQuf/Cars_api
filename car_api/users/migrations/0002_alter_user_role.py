# Generated by Django 4.2.2 on 2023-06-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.SmallIntegerField(choices=[(1, 'support'), (2, 'SALE')], default=2),
        ),
    ]