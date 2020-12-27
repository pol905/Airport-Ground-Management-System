from django.db import models
from postlog.models import FlightNum


class pnr(models.Model):
    pnr=models.CharField(max_length=9,primary_key=True)

    def __str__(self):
        return self.pnr



class passenger(models.Model):
    pnr=models.OneToOneField(pnr,on_delete=models.CASCADE,primary_key=True,related_name='p2')
    name=models.CharField(max_length=10)
    dob=models.DateField (auto_now=False, auto_now_add=False)
    passport_no= models.CharField(max_length=10,unique=True)
    fl_no=models.ForeignKey(FlightNum,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
