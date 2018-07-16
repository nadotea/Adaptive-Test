from django.conf.urls import url
from django.urls import re_path

from atest import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    # re_path(r'tests/$', views.tests, name='tests'),
    # (\d+)$
    re_path(r'test/', views.test, name='test'),
    # re_path(r'tests/(\d+)$', views.testInfo, name='testInfo'),
    # re_path(r'login/$', views.login, name='login'),
    re_path(r'about/$', views.about, name='about'),
    re_path(r'help/$', views.help, name='help'),
    # re_path(r'registration/$', views.registration, name='registration')
]

