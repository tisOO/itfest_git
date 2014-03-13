from django.contrib import admin
from itfest.tasks.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
	list_display = ('category', 'points','active', 'answer', 'hint')
	search_fields = ('category', 'points')
	
	
admin.site.register(Task, TaskAdmin)