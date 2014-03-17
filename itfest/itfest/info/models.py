# -*- coding: utf-8 -*-

from django.db import models
from itfest.users.models import Team




# Create your models here.

class News(models.Model):
	header = models.CharField(max_length = 128)
	text = models.TextField(max_length = 10000)
	time = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['time']
	
	def get_last_five_news(self):
		return News.objects.order_by('time')[0:5]
	def get_last_news(self):
		try:
			p = News.objects.order_by('time')[0]
		except IndexError:
			return u'No News'
		else:
			return p


class Chat(models.Model):
	text = models.CharField(max_length = 500)
	time = models.DateTimeField(auto_now_add=True)
	team = models.ForeignKey(Team)
	
	class Meta:
		ordering = ['time']


	def get_last_five_message(self):
		return Chat.objects.order_by('time')[0:5]
	def get_last_ten_message(self):
		return Chat.objects.order_by('-time')[0:10]



EVENT_CHOICES = (
	('TeamCompleted', 'Команда выполнила задание'),
	('TeamRadCard', 'Команда забанена'),
	('TeamYellowCard', 'Команда получила предупрждение'),
	('HintShow', 'Опубликована подсказка'),
	('TaskShow', 'Опубликовано задание'), 
	('AllComleted','Все задания выполнены'),
)


EVENTS = (
	(100, 'ура'),
	(200, 'qwe')
)

class Event_message(models.Model):
	situation = models.CharField(max_length = 10)
	text =  models.CharField(max_length = 128)

