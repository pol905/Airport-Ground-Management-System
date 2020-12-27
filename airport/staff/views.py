from django.shortcuts import render
from staff.models import Crew
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import crewForm
from django.contrib import messages


# Create your views here.

class CrewListPageView(ListView):
	
	model = Crew
	context_object_name = 'crews'
	template_name = 'staff/staff_home.html'

class CrewAddPageView(CreateView):
	
	template_name = "crew_add.html"
	model = Crew
	form_class = crewForm
	success_url = reverse_lazy('crew_list')

class CrewDeletePageView(DeleteView):

	model = Crew
	success_url = reverse_lazy('crew_list')

class CrewUpdatePageView(UpdateView):
    template_name = "crew_update.html"
    model = Crew
    form_class = crewForm
    success_url = reverse_lazy('crew_list')


def CrewSearch(request):
	if request.method =='POST':
		search_id =request.POST.get('textfield', None)
		creeks = Crew.objects.filter(crewid = search_id)
		args = {'creeks' : creeks }
		return render(request, 'crew_search.html', args)
	else:
		messages.warning(request, "This Employee does not exist.")
		return render(request, 'staff/staff_home.html')