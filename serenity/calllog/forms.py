from django.http import HttpResponse
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug, RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

import datetime

from .models import CallLog, CallLogType, Child
from clients.models import County, State, Clients


class Call_Log_Create(forms.ModelForm):
    call_log_type = forms.ModelChoiceField(queryset=CallLogType.objects.all())
    time_of_call = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    county_of_incident = forms.ModelChoiceField(queryset=County.objects.filter(avenues_support=1), required=True)
    first_name = forms.CharField(max_length=200,
        required=True,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='Caller First Name: Names can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    middle_init = forms.CharField(max_length=1,
        required=False,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='Caller Middle Name: Names can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    last_name = forms.CharField(max_length=200,
        required=True,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='Caller Last Name: Names can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )

    victims_name = forms.CharField(max_length=200,
        required=True,
        validators=[RegexValidator(
                        regex='^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$',
                        message='Victims Name: Names can only have letters, hypens, and apostrophies',
                        ),
                    ]
        )
    safe_call = forms.BooleanField(label='Is it safe to call back?', required = False)
    safe_phone_contact = forms.CharField(max_length=12, required = False)
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
    county_of_residence = forms.ModelChoiceField(queryset=County.objects.order_by('-avenues_support'), required=True)
    abusers_name = forms.CharField(max_length=200,
        required = False,
        label = 'Abuser\'s Name:',
    )
    abusers_city = forms.CharField(max_length=200,
        required = False,
        label = 'Abuser\'s City:',
    )
    immediate_danger = forms.BooleanField(label = 'Is the caller in immediate danger?', required=False)
    previous_victim_dv = forms.BooleanField(label = 'Have they ever been a victim of Domestic Violence?', required = False)
    dv_when = forms.CharField(required = False,
        label = 'If yes, when:'
    )
    previous_victim_sa = forms.BooleanField(label = 'Have they ever been a victim of Sexual Assault?', required = False)
    sa_when = forms.CharField(required = False,
        label = 'If yes, when:'
    )
    children = forms.BooleanField(label = 'Do you have any children?', required = False)
    num_children = forms.CharField(label = 'How many children do you have?',
        required = False
    )
    hear_about_avenues = forms.CharField(max_length=200, label = 'How did you hear about Avenues?', required = False)
    callback = forms.BooleanField(label = 'Do you require a call back?', required = False)
    by_whom = forms.ModelChoiceField(queryset=User.objects.all(),
        label = 'Call assigned to:',
        required=False,
        initial=4)
    call_length = forms.IntegerField()
    taken_by = forms.ModelChoiceField(queryset=User.objects.all(),
        label = 'Call logged by:')
    nature_of_problem = forms.CharField(max_length=200, required = False)
    previous_client = forms.BooleanField(label = 'Have you been a client of Avenues previously?', required = False)
    pc_when = forms.CharField(required = False,
        label = 'If yes\, when:'
    )
    client_id = forms.ModelChoiceField(queryset=Clients.objects.all(),
        required = False,
        label = 'Client: ',
        initial = 'NotAssigned'
    )
    call_notes = forms.CharField(widget=forms.Textarea, required = False)
    childern_info = forms.CharField(max_length=200, required = False)

    class Meta:
         model = CallLog
         fields = ( 'call_log_type', 'time_of_call', 'first_name', 'middle_init', 'last_name', 'victims_name', 'safe_call', 'safe_phone_contact', 'address_1', 'address_2', 'city', 'state',
            'county_of_residence', 'abusers_name', 'abusers_city', 'immediate_danger', 'previous_victim_dv', 'dv_when', 'previous_victim_sa', 'sa_when', 'children', 'num_children', 'hear_about_avenues',
            'callback', 'by_whom', 'call_length', 'taken_by', 'nature_of_problem', 'previous_client', 'pc_when', 'client_id', 'call_notes', 'children_info', 'county_of_incident' )

