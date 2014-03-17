from django.shortcuts import render_to_response
from django.template import loader, RequestContext

from itfest.users.models import Team
from itfest.info.models import News
from itfest.main.context_processors import itfest_proc
# Create your views here.



def view_team_list(request):
	return render_to_response("team_list.html", {}, context_instance = RequestContext(request, processors = [itfest_proc])) 

