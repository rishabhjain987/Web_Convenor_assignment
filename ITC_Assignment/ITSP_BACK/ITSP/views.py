from django.shortcuts import render

# Create your views here.
from .models import itsp_team

def itsp_home(request):
	itsp_team_name = itsp_team.objects.all()
	context = {'itsp_team_name' : obj.itsp_team_name}
	return render(request, 'ITSP/itsp_home_page.html',context)
