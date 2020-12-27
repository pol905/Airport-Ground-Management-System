from django import forms
from staff.models import Crew


class crewForm(forms.ModelForm):
	class Meta:
		model = Crew
		fields = ('crewid', 'name', 'crew_dob', 'company', 'role')
		labels = {
            'crewid': ('Staff ID'),
         	'name': ('Name'),
            'crew_dob': ('Date Of Birth(yyyy-mm-dd)'),
            'company': ('Company'),
            'role': ('Role'),
        }
