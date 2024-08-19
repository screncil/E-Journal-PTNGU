from django.contrib import admin

from .models import Grades
# Register your models here.

@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    list_display = ('grade', 'subject', 'student')
