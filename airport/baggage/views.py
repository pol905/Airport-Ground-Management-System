from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from baggage.forms import baggageForm, BaggageUpdateForm
from passenger.models import passenger
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from baggage.models import baggage
# Create your views here.
class baggageListPageView(ListView):

	model = baggage
	context_object_name = 'baggages'
	template_name = 'baggage/baggage_home.html'

class baggageAddPageView(CreateView):

	template_name = "baggage_add.html"
	model = baggage
	form_class = baggageForm
	success_url = reverse_lazy('baggage_list')

class baggageDeletePageView(DeleteView):

	model = baggage
	success_url = reverse_lazy('baggage_list')

class baggageUpdatePageView(UpdateView):
    
    template_name = "baggage/baggage_update.html"
    model = baggage
    form_class = BaggageUpdateForm
    success_url = reverse_lazy('baggage_list')

def baggageSearch(request):
	if request.method =='POST':
		search_id =request.POST.get('textfield', None)
		baggages = baggage.objects.filter(fl_no = search_id)
		args = {'baggages' : baggages }
		return render(request, 'baggage_search.html', args)
	else:
		messages.warning(request, "This Baggage does not exist.")
		return render(request, 'passenger/passenger_home.html')

def load_flight(request):
	pnrid = request.GET.get('pnr1')
	darks = passenger.objects.filter(pnr = pnrid).order_by('fl_no')
	context = {'darks': darks}
	return render(request, 'baggage/fl_no_dropdown.html', context)

def load_name(request):
	pnrid = request.GET.get('pnr2')
	cars = passenger.objects.filter(pnr = pnrid).order_by('name')
	context = {'cars': cars}
	return render(request, 'baggage/name_dropdown.html', context)
# create new function load_name
