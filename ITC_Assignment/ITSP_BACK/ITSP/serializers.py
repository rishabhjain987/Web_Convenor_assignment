from rest_framework import serializers
from .models import itsp_team

class itsp_teamSerializer(serializers.ModelSerializer):
	model = itsp_team
	fields = '__all__'