from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login_form(request):
	return render(request, 'login_page.html')

def submit_form(request):
	return HttpResponse("Welcome")