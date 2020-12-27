from django.db import models

# Create your models here.
class FlightNum(models.Model):
	fl_no =models.CharField(max_length=5,primary_key=True)

	def __str__(self):
		return self.fl_no

class Destination(models.Model):
	fl_no= models.OneToOneField(FlightNum,on_delete=models.CASCADE,related_name='fl1')
	dest= models.CharField(max_length=15,blank=True)

	def __str__(self):
		return self.dest

class Parking(models.Model):
	fl_no= models.OneToOneField(FlightNum,on_delete=models.CASCADE,related_name='fl2')
	park_bay= models.CharField(max_length=3, unique=True)

	def __str__(self):
		return self.park_bay

class DepartureTime(models.Model):
	fl_no= models.OneToOneField(FlightNum,on_delete=models.CASCADE,related_name='fl3')
	dep_time= models.CharField(max_length=9)

	def __str__(self):
		return self.dep_time

class Airline(models.Model):
	airline = models.CharField(max_length=35)

	def __str__(self):
		return self.airline

class Flight(models.Model):
	fl_no= models.OneToOneField(FlightNum,on_delete=models.CASCADE, primary_key=True, related_name='fl4')
	park_bay= models.ForeignKey(Parking, on_delete=models.CASCADE)
	dest= models.ForeignKey(Destination, on_delete=models.CASCADE)
	dep_time= models.ForeignKey(DepartureTime, on_delete=models.CASCADE)
	inbound= models.CharField(max_length=15,blank=True)
	airline= models.ForeignKey(Airline,max_length=15, on_delete=models.CASCADE)
	arr_time= models.TimeField(null=True, blank=True)
