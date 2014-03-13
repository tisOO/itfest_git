from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from itfest.users.models import Team




# Register your models here.
class TeamAdmin(admin.ModelAdmin):
#	add_form_template = 'admin/auth/user/add_form.html'
	list_display = ('username', 'points','last_task_time')
#	form = UserChangeForm
#	add_form = UserCreationForm
#	change_password_form = AdminPasswordChangeForm

#admin.site.unregister(User)
admin.site.register(Team, TeamAdmin)