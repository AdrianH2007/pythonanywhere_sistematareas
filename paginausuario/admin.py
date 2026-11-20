from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fiels = ("created")
admin.site.register(Task, TaskAdmin)
