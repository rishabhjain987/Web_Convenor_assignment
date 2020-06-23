from django.urls import path

from . import views

app_name = 'ITSP'
urlpatterns = [
	path('', views.itsp_home),
]