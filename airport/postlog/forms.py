from django.forms import ModelForm
from postlog.models import Flight, FlightNum, Destination, Parking, DepartureTime, Airline
from django import forms


class flightnoForm(ModelForm):
			class Meta:
				model = FlightNum
				fields = '__all__'
				labels = {
                    'fl_no' : ('Flight Number')
				}

class destForm(ModelForm):
			class Meta:
				model = Destination
				fields = ('dest',)
				labels = {
                    'dest' : ('Destination')
				}

			def save(self, a, commit=True):
				instance = super(destForm, self).save(commit=False)

				if not self.instance.pk:
                    # create
					if commit:
						instance.fl_no = a
						instance.save()
				return instance

class parkForm(ModelForm):
			class Meta:
				model = Parking
				fields = ('park_bay',)
				labels = {
                    'park_bay' : ('Parking Bay')
				}
			def save(self, a, commit=True):
				instance = super(parkForm, self).save(commit=False)

				if not self.instance.pk:
                    # create
					if commit:
						instance.fl_no = a
						instance.save()
				return instance	

class deptForm(ModelForm):
			class Meta:
				model = DepartureTime
				fields = ('dep_time',)
				labels = {
					'dep_time' : ("Departure Time (Enter 'None' if blank)")
				}

			def save(self, a, commit=True):
				instance = super(deptForm, self).save(commit=False)

				if not self.instance.pk:
                    # create
					if commit:
						instance.fl_no = a
						instance.save()
				return instance   

class flightForm(ModelForm):
			class Meta:
				model = Flight
				fields =('inbound','airline','arr_time')
				labels = {
					'airline' :('Airline'),
					'inbound' : ('Inbound'),
					'arr_time' : ('Arrival Time'),
				}
			def save(self, a, b, c, d, commit=True):
				instance = super(flightForm, self).save(commit=False)

				if not self.instance.pk:
                    # create
					if commit:
						instance.fl_no = a
						instance.park_bay = b
						instance.dest = c
						instance.dep_time = d
						instance.save()
				return instance