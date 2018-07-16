from sys import path

from django.conf.urls import url
from django.urls import re_path
from atest import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # re_path(r'tests/$', views.tests, name='tests'),
    # (\d+)$
    url(r'^register$', views.RegisterFormView.as_view(), name="register"),
    url(r'^login$', views.LoginFormView.as_view(), name="login"),
    url(r'^logout$', views.LogoutView.as_view(), name="logout"),
    re_path(r'^test/', views.test, name='test'),
    # re_path(r'tests/(\d+)$', views.testInfo, name='testInfo'),
    re_path(r'^about/$', views.about, name='about'),
    # re_path(r'^help/$', views.help, name='help'),
    # re_path(r'registration/$', views.registration, name='registration')
]

