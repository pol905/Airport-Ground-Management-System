from django.db import models
from postlog.models import Airline
# Create your models here.


class Crew(models.Model):
	crewid = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=15)
	crew_dob = models.DateField(auto_now=False, auto_now_add=False)
	company = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='al1')
	role = models.CharField(max_length=10)
