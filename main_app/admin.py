
from django.contrib import admin
from django.contrib.auth.models import User
from main_app.models import *


# Register your models here.
class Questionadmin(admin.ModelAdmin):
    list_display = ["user","title","content","created_at"]

class Answeradmin(admin.ModelAdmin):
    list_display = ["user","question","content","created_at"]

class Likeadmin(admin.ModelAdmin):
    list_display = ["user","answer"]

admin.site.register(Question,Questionadmin)
admin.site.register(Answer,Answeradmin)
admin.site.register(Like,Likeadmin)
    
