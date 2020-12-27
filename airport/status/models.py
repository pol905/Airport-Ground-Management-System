from django.db import models

# Create your models here.
from django.db import models
from postlog.models import FlightNum,Destination,Parking,DepartureTime

# Create your models here.
class FlightStatus(models.Model):
	CLEANING_CHOICES = (
		('Yes', 'Yes'),
		('No','No'),
	)
	fl_no= models.OneToOneField(FlightNum,on_delete=models.CASCADE,related_name='fli_no',primary_key=True)
	park_bay= models.ForeignKey(Parking,on_delete=models.CASCADE,related_name='parki_bay')
	catering= models.CharField(max_length=9)
	fuel= models.IntegerField()
	pas_cnt= models.IntegerField()
	dest= models.ForeignKey(Destination,on_delete=models.CASCADE,related_name='desti',null=True)
	dep_time=models.ForeignKey(DepartureTime,on_delete=models.CASCADE,related_name='dept_time')
	Cleaning = models.CharField( max_length=3, choices=CLEANING_CHOICES)

	class Meta:
		verbose_name_plural = 'Flight Status'
