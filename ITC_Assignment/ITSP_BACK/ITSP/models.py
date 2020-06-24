from django.db import models

# Create your models here.


class itsp_team(models.Model):
	Team_name  = models.CharField(max_length = 100)
	Team_ID    = models.CharField(max_length = 100)
	Member_1   = models.CharField(max_length = 100)
	Member_2   = models.CharField(max_length = 100)