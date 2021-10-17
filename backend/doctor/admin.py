from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(report)
class slo(admin.ModelAdmin):
    list_display = ['name','service','patient']