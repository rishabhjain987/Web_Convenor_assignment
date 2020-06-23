from django.db import models

# Create your models here.
class itsp_team_name(models.Model):
	team_name = models.CharField(max_length = 100)
	pub_date = models.DateTimeField('date published')


class itsp_team(models.Model):
	Team_name  = models.CharField(max_length = 100)
	Team_ID    = models.CharField(max_length = 100)
	Member_1   = models.CharField(max_length = 100)
	Member_2   = models.CharField(max_length = 100)