from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(User):
	points = models.PositiveSmallIntegerField(default = 0)
	last_task_time = models.DateTimeField(blank = True)
#	image = models.ImageField()

	#def __str__(self)
	