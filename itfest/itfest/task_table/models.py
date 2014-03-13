from django.db import models
from itfest.tasks.models import Task
from itfest.users.models import Team
# Create your models here.

class TaskTable(models.Model):
	team = models.ForeignKey(Team)	
	task = models.ForeignKey(Task)
	task_time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s %s %i' % (self.team.username, self.task.category, self.task.points)
	
	class Meta:
		ordering = ['task_time']
	
