from django.contrib import admin
from itfest.task_table.models import TaskTable
# Register your models here.


class TaskTableAdmin(admin.ModelAdmin):
	list_display = ('team', 'task', 'task_time')
	#list_filter = ('task_time')
	 
	#class Meta:
	#	ordering = ['-task_time']
                                     
admin.site.register(TaskTable, TaskTableAdmin)
