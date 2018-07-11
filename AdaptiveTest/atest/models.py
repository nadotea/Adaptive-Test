from django.db import models


class Answer(models.Model):
    parentQuestion = models.IntegerField()
    childrenQuestion = models.IntegerField()
    answer = models.TextField()

    def __str__(self):
        return self.answer


class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


class Result(models.Model):
    userId = models.IntegerField()
    testId = models.IntegerField()
    result = models.IntegerField()
    date = models.DateField()


class Test(models.Model):
    name = models.TextField()
    firstQuestion = models.IntegerField()
    num = models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.TextField()
    surname = models.TextField()
    email = models.EmailField(blank=True)
    name = models.TextField()
    age = models.IntegerField(blank=True)
    password = models.TextField()
    role = models.TextField(blank=True)

    def __str__(self):
        return self.username


