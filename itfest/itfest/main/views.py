#python
import datetime

#django
from django.shortcuts import render
from django.template import Context, loader

#itfest
from itfest.users.models import Team
from itfest.info.models import News, Chat
from itfest.task_table.models import TaskTable
from itfest.tasks.models import Task
# Create your views here.



def view_main(request, task_id = 0):
	#разбираем, что за запрос
	if request.method == 'POST':
		if request.POST.has_key('publish_chat'):
			#do something
		elif request.POST.has_key('check_answer'):
			#do something
		else:
			#Error message
	t = loader.get_template('tasks_page.html')
	news = News.get_last_five_news()
	try:
		task_ = Task.objects.get(id = task_id)
	except Task.DoesNotExist:
		task_ = Task.objects.get(id = 1)
	is_show_answer = False			#show form sending answer
	try:
		TaskTable.objects.get(task = task_, team = request.user))
	except TaskTable.DoesNotExist:
		is_show_answer = True
	c = Contex({
		'user', request.user,   #for cheking user and show some info about this user
		'team', Team,		#for list of teams
		'news', news,
		'task', task_,
		'tasks', tasks,
		'is_show_answer', is_show_answer,
		'task_id', task_id,
			
	})
	return t.render(c)