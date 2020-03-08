from django.contrib import admin
from .models import Position, Employee

class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'mobile','emp_code', 'position')

admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)