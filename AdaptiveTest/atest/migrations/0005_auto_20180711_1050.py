# Generated by Django 2.0.7 on 2018-07-11 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atest', '0004_auto_20180711_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.TextField(blank=True),
        ),
    ]
