from django.contrib import admin
from ToDoBeeDoBeeDoo.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ("description", "duedate", "done")

admin.site.register(Task, TaskAdmin)