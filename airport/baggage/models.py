from django.db import models

# Create your models here.
from django.db import models
from passenger.models import pnr,passenger
from postlog.models import Flight,FlightNum


class baggage(models.Model):
    pnr=models.ForeignKey(pnr,on_delete=models.CASCADE,related_name='bag_pnr')
    tag=models.CharField(max_length=8,unique=True)
    name=models.OneToOneField(passenger,on_delete=models.CASCADE,related_name='bag_name')
    fl_no=models.ForeignKey(FlightNum,on_delete=models.CASCADE,related_name='bag_flno')
