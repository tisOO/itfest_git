from django.shortcuts import render_to_response
from django.template import RequestContext
from itfest.info.models import News, Chat
from itfest.users.models import Team
from itfest.main.context_processors import itfest_proc

# Create your views here.


def view_news(request, count_news = 5):
	p = News.objects.order_by('-time', '-id')[0:count_news]
	#teams = Team.objects.order_by('-points', 'last_task_time')
	return render_to_response("news.html" ,{'news':p,}, context_instance = RequestContext(request, processors = [itfest_proc]))
	