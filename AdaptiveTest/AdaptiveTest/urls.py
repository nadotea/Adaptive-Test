"""AdaptiveTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import ListView, DetailView

# from atest import views
import atest
from atest.models import Test

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', atest.views.home, name='home'),
    url(r'^register/?$', atest.views.RegisterFormView.as_view(), name="register"),
    url(r'^login/?$', atest.views.LoginFormView.as_view(), name="login"),
    url(r'^logout/?$', atest.views.LogoutView.as_view(), name="logout"),
    url(r'^tests/?$', ListView.as_view(queryset=Test.objects.all(), template_name="aTest/"), name="tests"),
]
