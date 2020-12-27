from django.forms import ModelForm
from postlog.models import FlightNum
from passenger.models import pnr,passenger
from baggage.models import baggage

class baggageForm(ModelForm):
    class Meta:
        model = baggage
        fields = ('pnr','name','tag','fl_no')
        labels = {
            'pnr': ('Booking Reference Number'),
            'name': ('Name'),
            'tag': ('Tag'),
            'fl_no': ('Flight Number'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fl_no'].queryset = FlightNum.objects.none()
        self.fields['name'].queryset = passenger.objects.none()

        if 'pnr' in self.data:
            try:
                pnrid = int(self.data.get('pnr'))
                val = passenger.objects.filter(pnr=pnrid)
                val = val.values('fl_no')
                kick =[None]*val.count()
                for i in range(val.count()):
                    kick[i] =int(val[i].get('fl_no'))
                self.fields['fl_no'].queryset = FlightNum.objects.filter(fl_no__in=kick).order_by('fl_no')
                self.fields['name'].queryset = passenger.objects.filter(pnr=pnrid).order_by('name')
            except (ValueError, TypeError):
                pass

class BaggageUpdateForm(ModelForm):
    class Meta:
        model = baggage
        fields = ('pnr','name','tag','fl_no')
        labels = {
            'pnr': ('Booking Reference Number'),
            'name': ('Name'),
            'tag': ('Tag'),
            'fl_no': ('Flight Number'),
        }