from django.shortcuts import render
from django.template import loader, RequestContext

from itfest.users.models import Team

# Create your views here.



def view_team_list(request):
	p = Team.objects.order_by('-points')
	print p
	return render(request, 'teams.html', {'teams':p}) 

