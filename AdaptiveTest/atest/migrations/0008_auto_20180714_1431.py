# Generated by Django 2.0.7 on 2018-07-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atest', '0007_test_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('surname', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('name', models.TextField()),
                ('age', models.IntegerField(blank=True)),
                ('password', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='result',
            name='date',
        ),
        migrations.RemoveField(
            model_name='result',
            name='result',
        ),
        migrations.RemoveField(
            model_name='result',
            name='testId',
        ),
        migrations.RemoveField(
            model_name='test',
            name='num',
        ),
        migrations.AddField(
            model_name='result',
            name='answer',
            field=models.ForeignKey(null='false', on_delete='null', related_name='Answers', to='atest.Answer'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='childrenQuestion',
            field=models.ForeignKey(blank='true', null='true', on_delete='null', related_name='ChildrenQuestion', to='atest.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='parentQuestion',
            field=models.ForeignKey(null='false', on_delete='null', related_name='ParentQuestion', to='atest.Question'),
        ),
        migrations.AlterField(
            model_name='result',
            name='userId',
            field=models.ForeignKey(null='false', on_delete='null', related_name='Users', to='atest.UserProfile'),
        ),
        migrations.AlterField(
            model_name='test',
            name='firstQuestion',
            field=models.ForeignKey(on_delete='null', related_name='Questions', to='atest.Question'),
        ),
    ]