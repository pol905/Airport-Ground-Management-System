from django.shortcuts import render
from django.http import HttpResponse
from postlog.models import Flight, DepartureTime

def HomePageView(request):
	val = DepartureTime.objects.exclude(dep_time__iexact='None')
	val = val.values('fl_no')
	link = [None]*val.count()
	for i in range(val.count()):
		link[i] =int(val[i].get('fl_no'))
	cons = Flight.objects.filter(fl_no__in = link).order_by('fl_no')
	disks = Flight.objects.exclude(arr_time = None).order_by('fl_no')
	args = { 'cons' : cons, 'disks' : disks }
	return render(request, 'base_home.html', args)

def Homeview(request):
	return render(request,'home.html') 
