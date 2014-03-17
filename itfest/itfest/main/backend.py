# -*- coding: utf-8 -*-

#python
import datetime

#django
from django.shortcuts import render
from django.template import Context, loader
from django.http import Http404
from django.contrib.auth.hashers import (
    check_password, make_password, is_password_usable)
#itfest
from itfest.users.models import Team
from itfest.info.models import News, Chat, Event_message
from itfest.task_table.models import TaskTable
from itfest.tasks.models import Task, GameTime
# Create your views here.
from django.utils import timezone


#for activating Tasks
def activeTask():
	tasks = Task.objects.filter(displaytime__lt = datetime.datetime.now(), active = False)
	for one_task in tasks:
		one_task.active = True
		one_task.save()
		add_news_about_adding_task_time(one_task)
			
#for showing hints
def showHint():
	tasks = Task.objects.filter(hint_display_time__lte = datetime.datetime.now(), is_show_hint = False)
	for one_task in tasks:
		one_news = News(header = ('Подсказка к заданию №'+str(one_task.id)), text = one_task.hint)
		one_news.save()
		one_task.is_show_hint = True
		one_task.save()

#recalclualtion points
def recalc_points():
		teams = Team.objects.all()
		for cur_team in teams:
			complited_tasks = TaskTable.objects.filter(team = cur_team)
			cur_team.points = 0
			for complited_task in complited_tasks:
				cur_team.points += complited_task.task.points
			cur_team.save()

def check_psw(cur_task, raw_password):
	def setter(raw_password):
		cur_task.answer = make_password(raw_password)
		cur_task.save()
	return check_password(raw_password,cur_task.answer,setter)	

#when some team finished task, we must say about it for all teams
def add_news_about_complited(cur_team, cur_task):
	try:
		message = Event_message.objects.get(situation = 'complited').text %(cur_team.username, cur_task.header)
	except Event_message.DoesNotExist:
		#defualt message
		message = u'Были обнаружены улики командой %s. Они справились с заданием "%s"'%(cur_team.username, cur_task.header)
	news = News(header = 'Внимание', text = message)
	news.save()

#add news about adding task thanks to time
def add_news_about_adding_task_time(new_task):
	try:
		message = Event_message.objects.get(situation = 'a_tasktime').text %(new_task.header)
	except Event_message.DoesNotExist:
		message = u'Время поджимает. Опубликовано задание "%s"' %(new_task.header)
	news = News(header = 'Опубликовано задание', text = message)
	news.save()

#add news about adding task thanks to some team
def add_news_about_adding_task_team(new_task):
	try:
		message = Event_message.objects.get(situation = 'a_taskteam').text %(new_task.header)
	except Event_message.DoesNotExist:
		message = u'Время поджимает. Опубликовано задание "%s"' %(new_task.header)
	news = News(header = 'Опубликовано задание', text = message)
	news.save()

def active_next_task(cur_task):
	try:
		next_task = Task.objects.get(id = (cur_task.id + 1), active = False)
	except Task.DoesNotExist:
		None
	else:
		next_task.active = True
		next_task.save()
		add_news_about_adding_task_team(next_task)
		
	
	
	
#checking answer
'''
task_ - current task
cur_team  - current_team
'''
def check_answer(request, task_, cur_team):
	if request.method == 'POST':						#maybe some guy has answer
		user_answer = request.POST['answer']
		if not user_answer:
			print 'pechal_beda'
		else:
			user_answer = user_answer.upper()
			cur_task = Task.objects.get(id = task_.id)
			
			if (check_psw(cur_task, user_answer)):
				#correct answer
				print '=)'
				cur_team.last_task_time = datetime.datetime.now()
				new_record_in_TaskTable = TaskTable(team = cur_team, task = task_, )
				new_record_in_TaskTable.save()
				cur_team.points += task_.points
				cur_team.save()
				add_news_about_complited(cur_team, task_)
				active_next_task(task_)
				return False
			else:
				#incorrect answer
				print '=('
	return True
