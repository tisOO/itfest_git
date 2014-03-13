from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(User):
	points = models.PositiveSmallIntegerField(default = 0, blank = True, null = True)
	last_task_time = models.DateTimeField(blank = True, null = True)
	image = models.URLField(blank = True, null = True)
#	image = models.ImageField(upload_to = '/photos/', null = True, blank = True)

	#def __str__(self)

# models.py
