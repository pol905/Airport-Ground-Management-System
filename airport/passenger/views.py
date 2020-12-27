from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from passenger.forms import passForm, passenForm, pnrForm
from passenger.models import passenger, pnr
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from postlog.models import Flight
from django.contrib import messages
from django.urls import reverse_lazy,reverse
# Create your views here.
class passengerListPageView(ListView):

	model = passenger
	context_object_name = 'passengers'
	template_name = 'passenger/passenger_home.html'

#class passengerAddPageView(CreateView):

#	template_name = "passenger_add.html"
#	model = passenger
#	form_class = passForm
#	success_url = reverse_lazy('passenger_list')

class passengerDeletePageView(DeleteView):

	model = pnr
	success_url = reverse_lazy('passenger_list')

class passengerUpdatePageView(UpdateView):
    template_name = "passenger_update.html"
    model = passenger
    form_class = passForm
    success_url = reverse_lazy('passenger_list')

def passengerSearch(request):
	if request.method =='POST':
		search_id =request.POST.get('textfield', None)
		weeks = passenger.objects.filter(fl_no = search_id)
		args = {'weeks' : weeks }
		return render(request, 'passenger_search.html', args)
	else:
		messages.warning(request, "This Passenger does not exist.")
		return render(request, 'passenger/passenger_home.html')


def passengerAdd(request):
		if request.method =="POST":
			formA = pnrForm(request.POST, prefix= 'pnr')
			formC = passenForm(request.POST, prefix= 'pass')
			if formA.is_valid() and formC.is_valid():
				a = formA.save()
				c = formC.save(a)
				return redirect(reverse('passenger_list'))
		else:
			formA = pnrForm(prefix = 'pnr')
			formC = passenForm(prefix = 'pass')
		args = {'formA' : formA, 'formC' : formC}
		return render(request, 'passenger_add.html', args)
