# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.hashers import make_password
#import bcrypt
import datetime
from itfest.info.models import News
# Create your models here.

CATEGORY_CHOICES = (
	('Crypto', 'Crypto'),
	('Stegastic', 'Stegano'),
	('PNC', 'Professional Noob coding'),
	('Joy', 'JOY'),
)

POINTS_CHOICES = (
	(100, '100'),
	(200, '200'),
	(300, '300'),
	(400, '400'),
	(500, '500')
)

class Task(models.Model):
	header = models.CharField(max_length = 128)
	text = models.TextField()

#	image = models.ImageField()
	category = models.CharField(max_length = 15, choices = CATEGORY_CHOICES)
	points = models.PositiveSmallIntegerField(choices = POINTS_CHOICES)
	displaytime = models.DateTimeField()
	active = models.BooleanField(default = False)
	answer = models.CharField('answer', max_length = 100)
	hint = models.CharField(max_length = 200, blank = True)
	hint_display_time = models.DateTimeField(blank = True, null = True)
	is_show_hint = models.BooleanField(default = False)
	def __unicode__(self):
		return u'%s %i' %(self.category, self.points)
		
	def save(self, *args,**kwargs):
		#self.set_answer(kwargs['answer'])
		#print args
		#print kwargs
		#print self
		self.answer = self.answer.upper()
		self.set_answer(self.answer)
		super(Task, self).save(*args, **kwargs)
		
		
		
	def set_answer(self, raw_answer):
		self.answer = make_password(raw_answer)
                                  
	
	class Meta:
		ordering = ['id']

class GameTime(models.Model):
	event = models.CharField(max_length = 128)	
	time = models.DateTimeField()

	def __unicode__(self):
		return u'%s' %(self.event)
	class Meta:
		ordering = ['id']
