from django.forms import ModelForm
from status.models import FlightStatus
from postlog.models import FlightNum,Destination,Parking,DepartureTime

class StatusForm(ModelForm):
    class Meta:
        model = FlightStatus
        fields = ('fl_no', 'park_bay', 'catering', 'fuel', 'pas_cnt', 'dest','dep_time', 'Cleaning')
        labels = {
            'fl_no': ('Flight Number'),
            'park_bay': ('Parking Bay'),
            'catering': ('Catering (Veg:Non-Veg)'),
            'fuel': ('Fuel'),
            'pas_cnt': ('Passenger Count'),
            'dest': ('Destination'),
            'dep_time': ('Departure Time'),
            'Cleaning': ('Cleaning'),    
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['park_bay'].queryset = Parking.objects.none()
        self.fields['dest'].queryset = Destination.objects.none()
        self.fields['dep_time'].queryset = DepartureTime.objects.none()

        if 'fl_no' in self.data:
            try:
                flightid = int(self.data.get('fl_no'))
                self.fields['park_bay'].queryset = Parking.objects.filter(fl_no=flightid).order_by('park_bay')
                self.fields['dest'].queryset = Destination.objects.filter(fl_no=flightid).order_by('dest')
                self.fields['dep_time'].queryset = DepartureTime.objects.filter(fl_no=flightid).order_by('dep_time')
            except (ValueError, TypeError):
                pass



class StatusUpdateForm(ModelForm):
	class Meta:
		model = FlightStatus
		fields = ('fl_no', 'park_bay', 'catering', 'fuel', 'pas_cnt', 'dest','dep_time', 'Cleaning')
		labels = {
            'fl_no': ('Flight Number'),
         	'park_bay': ('Parking Bay'),
            'catering': ('Catering (Veg:Non-Veg)'),
            'fuel': ('Fuel'),
            'pas_cnt': ('Passenger Count'),
            'dest': ('Destination'),
            'dep_time': ('Departure Time'),
            'Cleaning': ('Cleaning'),    
        }