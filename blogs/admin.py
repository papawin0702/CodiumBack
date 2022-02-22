from django.contrib import admin
from . import models

# Register your models here.

class PostAdminModel(admin.ModelAdmin):
    list_display = ("name","published")

admin.site.register(models.Post,PostAdminModel)