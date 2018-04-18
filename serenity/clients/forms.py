from django.http import HttpResponse
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug, RegexValidator
from .models import Clients, Demographics, Type, Gender, County, AbuseType, Ethnicity, State, Status
from neighborhoodwatch.models import Perps
from django.utils.translation import ugettext_lazy as _
import datetime

def validate_slugs(self):
        data = self.cleaned_data['first_name']
        try:
            validate_slug(data)
        except ValidationError:
            err = _('No special characters other than hypens and apostrophies are allowed')
            return HttpResponse(err)

class ClientInsertTest(forms.ModelForm):
    client_number = forms.CharField(max_length=50)
    client_type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True)
    demographics = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Demographics.objects.all(), required=True)
    first_name = forms.CharField(max_length=200,
        required=True,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='Client First Name: Names can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    middle_init = forms.CharField(max_length=1,
        required=False,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='Client Middle Name: Names can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    last_name = forms.CharField(max_length=200,
        required=True,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='Client Last Name: Names can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), required=True)
    county_of_incident = forms.ModelChoiceField(queryset=County.objects.filter(avenues_support=1))
    abusetype = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=AbuseType.objects.all())
    ethnicity = forms.ModelChoiceField(queryset=Ethnicity.objects.all(), required=True)
    dob = forms.DateField(input_formats=['%d-%m-%Y'])
    #age = forms.CharField(max_length=3)
    address_1 = forms.CharField(max_length=200,
        required=False,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='Address: Addresses can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    address_2 = forms.CharField(max_length=200,
        required=False,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='Address: Addresses can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    city = forms.CharField(max_length=200,
        required=False,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='City: Cities can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    state = forms.ModelChoiceField(queryset=State.objects.all(), initial=25, required=False)
    status_id = forms.ModelChoiceField(queryset=Status.objects.all())
    date_of_first_contact = forms.DateField(input_formats=['%d-%m-%Y'])
    county_of_residence = forms.ModelChoiceField(queryset=County.objects.order_by('-avenues_support'), required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    primary_victim = forms.ModelChoiceField(queryset=Clients.objects.filter(client_type=1), required=True)
    emergency_contact_name = forms.CharField(max_length=200,
        required=False,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='Client Emergency Contact: Names can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    emergency_contact_phone = forms.CharField(max_length=15, required=False)
    perp = forms.ModelChoiceField(queryset=Perps.objects.all(), required=False)
    perp_relationship = forms.CharField(max_length=50, required=False)


    def clean_date_of_first_contact(self):
        data = self.cleaned_data['date_of_first_contact']

        #Check date is not in past.
        if data > datetime.date.today():
            raise forms.ValidationError(_("Invalid date - date in the future"))

        return data


    def clean_dob(self):
        data = self.cleaned_data['dob']

        if data > datetime.date.today():
            raise forms.ValidationError(_("Invalid date - date in the future"))

        return data


    class Meta:
         model = Clients
         fields = ( 'client_number', 'client_type', 'first_name', 'middle_init', 'last_name',
            'gender', 'county_of_incident', 'demographics', 'abusetype', 'ethnicity', 'dob', 'address_1',
            'address_2', 'city', 'state', 'date_of_first_contact', 'status_id', 'county_of_residence',
            'phone_number', 'primary_victim', 'emergency_contact_name', 'emergency_contact_phone', 'perp', 'perp_relationship'  )

