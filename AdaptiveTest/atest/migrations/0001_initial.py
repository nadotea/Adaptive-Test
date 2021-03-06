# Generated by Django 2.0.7 on 2018-07-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('parentQuestion', models.IntegerField()),
                ('childrenQuestion', models.IntegerField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userId', models.IntegerField()),
                ('testId', models.IntegerField()),
                ('result', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('firstQuestion', models.IntegerField()),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('surname', models.TextField()),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('password', models.TextField()),
                ('role', models.TextField()),
            ],
        ),
    ]
