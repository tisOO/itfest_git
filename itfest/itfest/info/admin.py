from django.contrib import admin
from itfest.info.models import News, Chat, Event_message
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
	list_display = ('header','time',)
	search_fields = ('header','time',)	

class ChatAdmin():
	list_display = ('team', 'text', 'time')
	search_fields = ('team', 'time')

class Event_messageAdmin(admin.ModelAdmin):
	list_display = ('situation', 'text')
                                               	
	
admin.site.register(News, NewsAdmin)
admin.site.register(Chat)
admin.site.register(Event_message, Event_messageAdmin)