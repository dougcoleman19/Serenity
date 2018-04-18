from django import forms
from .models import Room, Bed, BedSize

from clients.models import Clients


class RoomUpdate(forms.ModelForm):
    bed_id = forms.CharField()
    room_id = forms.ModelChoiceField(queryset=Room.objects.all())
    bed_size = forms.ModelChoiceField(queryset=BedSize.objects.all(), required=False)
    client_assigned = forms.ModelChoiceField(queryset=Clients.objects.all(), required=False)

    #def __init__(self, *args, **kwargs):
        #super(RoomUpdate, self).__init__(*args, **kwargs)
        #self.fields['client_assigned'].choices.insert(0, ('','---------' ) )

    class Meta:
         model = Bed
         fields = ('bed_id', 'client_assigned', 'room_id', 'bed_size' )