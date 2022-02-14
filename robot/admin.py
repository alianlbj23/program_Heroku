from django.contrib import admin
from robot.models import *

class gameAdmin(admin.ModelAdmin):
    list_display = ['title','text']
admin.site.register(game, gameAdmin)
# Register your models here.
