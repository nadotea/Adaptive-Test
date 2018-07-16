from datetime import datetime

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


class Test(models.Model):
    name = models.TextField()
    firstQuestion = models.ForeignKey('Question', on_delete='null',
                                      related_name='Questions')
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name


class TestSession(models.Model):
    userID = models.ForeignKey(User, on_delete='null',
                               related_name='Users',
                               null='false')
    testID = models.ForeignKey(Test, on_delete='null',
                               related_name='PassingTests',
                               null='false')


class UsersAnswers(models.Model):
    date = models.DateTimeField(default=datetime.now())
    sessionID = models.ForeignKey(TestSession, on_delete='null',
                                  related_name='Sessions',
                                  null='false')
    questionID = models.ForeignKey(Question, on_delete='null',
                                   related_name='SessionQuestions',
                                   null='false')
    answersID = models.ForeignKey(Answer, on_delete='null',
                                  related_name='SessionAnswers',
                                  null='false')



