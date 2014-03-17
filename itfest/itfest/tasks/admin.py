from django.contrib import admin
from itfest.tasks.models import Task, GameTime

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
	list_display = ('id','category', 'points', 'header','active', 'answer', 'hint')
	search_fields = ('category', 'points')
	

class GameTimeAdmin(admin.ModelAdmin):
	list_display = ('event', 'time')
	
admin.site.register(Task, TaskAdmin)
admin.site.register(GameTime, GameTimeAdmin)