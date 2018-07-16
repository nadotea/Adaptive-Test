from django.contrib.auth.models import User
from django.db import models


class Answer(models.Model):
    answer = models.TextField()
    parentQuestion = models.ForeignKey('Question', on_delete='null',
                                       related_name='ParentQuestion',
                                       null='false')

    childrenQuestion = models.ForeignKey('Question', blank='true', on_delete='null',
                                         related_name='ChildrenQuestion',
                                         null='true')

    def __str__(self):
        return self.answer


class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


class Result(models.Model):
    userId = models.ForeignKey('UserProfile', on_delete='null',
                               related_name='Users',
                               null='false')
    answer = models.ForeignKey('Answer', on_delete='null',
                               related_name='Answers',
                               null='false')


class Test(models.Model):
    name = models.TextField()
    firstQuestion = models.ForeignKey('Question', on_delete='null',
                                      related_name='Questions')
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete='null',
                             related_name='Users',
                             null='false')
    username = models.TextField()
    surname = models.TextField()
    email = models.EmailField(blank=True)
    name = models.TextField()
    age = models.IntegerField(blank=True)
    password = models.TextField()

    def __str__(self):
        return self.username


