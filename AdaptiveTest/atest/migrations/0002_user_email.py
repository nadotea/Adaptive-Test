# Generated by Django 2.0.7 on 2018-07-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]