from django.db import models
from itfest.users.models import Team

# Create your models here.

class News(models.Model):
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