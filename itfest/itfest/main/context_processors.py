from django.core.context_processors import request
from django.template import RequestContext
from django.shortcuts import render_to_response 
from django.utils import timezone

from itfest.info.models import News
from itfest.users.models import Team
from itfest.tasks.models import GameTime

def itfest_proc(request):
	print '=)'
	news = News.objects.order_by('-time', '-id')[0:5]
	teams = Team.objects.order_by('-points', 'last_task_time')
	try:
		finish_time = GameTime.objects.get(event = 'finish')
	except GameTime.DoesNotExist:
		finish_time = timezone.now()
	return {
		'cur_news': news,
		'teams':teams,
		'finish_time': finish_time,
	}