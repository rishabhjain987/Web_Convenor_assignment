from django.urls import path

from . import views

app_name = 'ITSP'
urlpatterns = [
    path('', views.itsp_home),
    path('<str:my_id>/', views.dynamic_view, name="ITSP")
]
