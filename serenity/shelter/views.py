from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template import loader
from django.db import IntegrityError

from .models import Room, Bed, Shelter
from .forms import RoomUpdate


def index(request):
    rooms = Room.objects.order_by('shelter_id')
    beds = Bed.objects.all()
    shelter = Shelter.objects.all()
    template = loader.get_template('shelter/index.html')
    context = {
        'rooms': rooms,
        'beds':beds,
        'shelter':shelter,
    }
    return HttpResponse(template.render(context, request))


def room_update(request, pk, template_name='shelter/room_edit.html'):
    beds = get_object_or_404(Bed,pk=pk)
    form = RoomUpdate(request.POST or None, instance=beds)
    try:
        if form.is_valid():
            form.save()
            return redirect('/shelter/')
    except IntegrityError as e:
        return render_to_response(template_name, {'message': e.__cause__ })
    return render(request, template_name, {'form': form, 'beds':beds,})
