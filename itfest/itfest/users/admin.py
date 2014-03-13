from django.contrib import admin
from itfest.users.models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'points','last_task_time')
	search_fields = ('name', 'points')

admin.site.register(Team)