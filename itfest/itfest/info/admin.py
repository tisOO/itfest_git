from django.contrib import admin
from itfest.info.models import News, Chat
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
	list_display = ('time',)
	search_fields = ('time',)	

class ChatAdmin():
	list_display = ('team', 'text', 'time')
	search_fields = ('team', 'time')


                                               	
	
admin.site.register(News)
admin.site.register(Chat)