from django.forms import ModelForm
from postlog.models import FlightNum
from passenger.models import pnr,passenger

class passForm(ModelForm):
    class Meta:
        model = passenger
        fields = ('pnr','name','passport_no','dob','fl_no')
        labels = {
            'pnr': ('Booking Reference Number'),
            'name': ('Name'),
            'dob': ('Date of Birth'),
            'passport_no': ('passport Number'),
            'fl_no': ('Flight Number'),
        }

class pnrForm(ModelForm):
            class Meta:
                model = pnr
                fields = '__all__'
                labels = {
                    'pnr' : ('PNR')
                }


class passenForm(ModelForm):
            class Meta:
                model = passenger
                fields = ('name','dob', 'passport_no', 'fl_no')
                labels = {
                    'name' : ('Name'),
                    'dob' : ('Date Of Birth(yyyy-mm-dd)'),
                    'passport_no' : ('Passport Number'),
                    'fl_no' : ('Flight Number'),
                }

            def save(self, a, commit=True):
                instance = super(passenForm, self).save(commit=False)
                if not self.instance.pk:
# create
                    if commit:
                        instance.pnr = a

                        instance.save()
                return instance
