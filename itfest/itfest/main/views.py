# -*- coding: utf-8 -*-

#python
import datetime

#django
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.hashers import (
    check_password, make_password, is_password_usable)
from django.contrib import auth	

#itfest
from itfest.users.models import Team
from itfest.info.models import News, Chat
from itfest.task_table.models import TaskTable
from itfest.tasks.models import Task, GameTime
# Create your views here.
from django.utils import timezone

from itfest.main.backend import activeTask, showHint, recalc_points, check_psw, check_answer
from itfest.main.context_processors import itfest_proc

def context_proc(request):
	teams = Team.objects.order_by('-points', 'last_task_time')
	news = News.objects.order_by('-time')
	try:
		final_time = GameTime.objects.get(event = 'finish')
	except GameTime.DoesNotExist:
		final_time = timezone.now()
	return {
		'teams':teams,
		'cur_news':news,
		'final_time':final_time,
	}
	
def view_task(request, task_id = 0):
	recalc_points()
	try:
		GameTime.objects.get(event = 'start', time__lte = timezone.now())
	except GameTime.DoesNotExist:
		#raise Http404()
		task_ = None
		active_tasks = []
		is_show_answer = False
	else:			
		activeTask()
		showHint()
		try:
			task_ = Task.objects.get(id = task_id)
		except Task.DoesNotExist:
			task_ = Task.objects.get(id = 1)
		#we have time? or it's finish
		try:
			GameTime.objects.get(event = 'finish', time__lte = timezone.now())
		except GameTime.DoesNotExist:
			is_show_answer = False			#show form sending answer
			try:
				cur_team = Team.objects.get(id = request.user.id)	#checking: is team user or not?
			except Team.DoesNotExist:
				is_show_answer = False								#if not, don't show answer_form
			else:
				#is answer in table?
				try:
					t = TaskTable.objects.get(task = task_, team = cur_team)
				except TaskTable.DoesNotExist:							#hasn't answer in table
					is_show_answer = check_answer(request, task_, cur_team)		
		else:
			is_show_answer = False
		active_tasks = Task.objects.filter(active = True).order_by('displaytime')
					
		
			
	#p = Team.objects.order_by('-points')
	
	news_ = News.objects.order_by('-time')[0:5]
	
	#c = RequestContext(request, processors = [itfest_proc])
	return render_to_response('tasks_page.html', { 
		'user':request.user, 
		'active_tasks':active_tasks,
		'cur_task': task_,
		'is_show_answer':is_show_answer}, context_instance = RequestContext(request, processors = [itfest_proc]))
				


def view_rules(request):
	return render_to_response("rules.html",{}, context_instance = RequestContext(request, processors = [itfest_proc]))
	
def view_contacts(request):
	return render_to_response("contacts.html",{}, context_instance = RequestContext(request, processors = [itfest_proc]))
	
def view_main(request):
	#teams = Team.objects.order_by('-points', 'last_task_time')
	return render_to_response("main.html",{}, context_instance = RequestContext(request, processors = [itfest_proc]))
	
def view_logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
	
