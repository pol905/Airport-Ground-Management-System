from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from status.forms import StatusUpdateForm, StatusForm
from status.models import FlightStatus
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from postlog.models import Flight
from django.urls import reverse_lazy



class StatusListPageView(ListView):
    model = FlightStatus
    context_object_name = 'ranks'
    template_name = 'status_home.html'

class StatusDeletePageView(DeleteView):
	model = FlightStatus
	success_url = reverse_lazy('status_list')

class StatusUpdatePageView(UpdateView):
    template_name = "status_update.html"
    model = FlightStatus
    form_class = StatusUpdateForm
    success_url = reverse_lazy('status_list')

class StatusAddPageView(CreateView):

	template_name = "status_add.html"
	model = FlightStatus
	form_class = StatusForm
	success_url = reverse_lazy('status_list')


def SearchKey(request):
	if request.method =='POST':
		search_id =request.POST.get('textfield', None)
		flecks = FlightStatus.objects.filter(fl_no = search_id)
		args = {'flecks' : flecks }
		return render(request, 'status_result.html', args)
	else:
		return render(request, 'status_home.html')

def load_park_bay(request):
	flightid = request.GET.get('flight1')
	parks = Flight.objects.filter(fl_no=flightid).order_by('park_bay')
	context = {'parks': parks}
	return render(request, 'status/park_bay_dropdown_list.html', context)

def load_destination(request):
	flightid = request.GET.get('flight2')
	dests = Flight.objects.filter(fl_no=flightid).order_by('dest')
	context = {'dests': dests}
	return render(request, 'status/dest.html', context)

def load_departure(request):
	flightid = request.GET.get('flight3')
	depts = Flight.objects.filter(fl_no=flightid).order_by('dep_time')
	context = {'depts': depts}
	return render(request, 'status/dept.html', context)
