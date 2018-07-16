from django.contrib import admin
from .models import *

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TestSession)
admin.site.register(UsersAnswers)
admin.site.register(Test)
# Register your models here.
