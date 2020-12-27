from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from postlog.models import Flight, FlightNum
from django.urls import reverse_lazy,reverse
from postlog.forms import flightnoForm, deptForm, parkForm, destForm, flightForm
from django.contrib import messages
from django.shortcuts import render,redirect
# Create your views here.

class FlightListPageView(ListView):

	model = Flight
	context_object_name = 'brakes'
	template_name = 'postlog/flight_home.html'

class FlightDeletePageView(DeleteView):

	model = FlightNum
	success_url = reverse_lazy('flight_list')

def FlightSearchPageView(request):
	if request.method =='POST':
		search_id =request.POST.get('textfield', None)
		wakes = Flight.objects.filter(fl_no = search_id)
		args = {'wakes' : wakes }
		return render(request, 'flight_search.html', args)
	else:
		messages.warning(request, "This Flight does not exist.")
		return render(request, 'postlog/flight_search.html')

def FlightAddPageView(request):
		if request.method =="POST":
			formA = flightnoForm(request.POST, prefix= 'flno')
			formB = parkForm(request.POST, prefix= 'park')
			formC = destForm(request.POST, prefix= 'dest')
			formD = deptForm(request.POST, prefix= 'dept')
			formE = flightForm(request.POST, prefix= 'figh')
			if formA.is_valid() and formB.is_valid() and formC.is_valid() and formD.is_valid() and formE.is_valid():
				a = formA.save()
				b = formB.save(a)
				c = formC.save(a)
				d = formD.save(a)
				e = formE.save(a, b, c, d)
				return redirect(reverse('flight_list'))
		else:
			formA = flightnoForm(prefix= 'flno')
			formB = parkForm(prefix= 'park')
			formC = destForm(prefix= 'dest')
			formD = deptForm(prefix= 'dept')
			formE = flightForm(prefix= 'figh')
		args = {'formA' : formA, 'formB': formB, 'formC' : formC, 'formD' : formD, 'formE' : formE}
		return render(request, 'flight_add.html', args)
