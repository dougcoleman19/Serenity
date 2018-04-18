from django.http import HttpResponse
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug, RegexValidator
from .models import Perps, Status
from django.utils.translation import ugettext_lazy as _


class PerpCreate(forms.ModelForm):
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
                        message='Client First Name: Names can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    last_name = forms.CharField(max_length=200,
        required=True,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='Client First Name: Names can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    birthdate = forms.CharField(max_length=15, required=False)
    date_created = forms.CharField(max_length=15 , required=False)
    status_id = forms.ModelChoiceField(queryset=Status.objects.all())


    class Meta:
         model = Perps
         fields = ( 'first_name', 'middle_init', 'last_name', 'birthdate', 'date_created', 'status_id' )