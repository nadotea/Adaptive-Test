from django.shortcuts import render
from django.contrib import auth


def homepage(request):
    return render(request,
                  'aTest/homepage.html',
                  locals())


def testinfo(request):
    return


def test(request):
    return render(request,
                  'aTest/test.html',
                  locals())


def about(request):
    return render(request,
                  'aTest/about.html',
                  locals())


def help(request):
    return render(request,
                  'aTest/help.html',
                  locals())
