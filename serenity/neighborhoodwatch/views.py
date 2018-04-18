from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
#from django.forms import ModelForm
#from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required#, permission_required

from .models import Perps
from .forms import PerpCreate

@login_required
def index(request):
    latest_perp_list = Perps.objects.order_by('-perp_id')[:5]
    template = loader.get_template('neighborhoodwatch/index.html')
    context = {
        'latest_perp_list': latest_perp_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, perp_id):
    try:
        perp = Perps.objects.get(pk=perp_id)
        #calllog = CallLog.objects.get(pk=client_id)
        #latest_calllog = CallLog.objects.order_by('-date_received').filter(client_id_id=client_id)
        context = { 'perp': perp }
        template = loader.get_template('neighborhoodwatch/detail.html')
    except Perps.DoesNotExist:
        raise Http404("Perp does not exist")
    return HttpResponse(template.render(context, request))


def perp_create(request):
    if request.method == "POST":
        form = PerpCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/neighborhoodwatch/')
    else:
        form = PerpCreate()
    return render(request, 'neighborhoodwatch/new.html', {'form':form})


def perp_update(request, pk, template_name='neighborhoodwatch/new.html'):
    perp = get_object_or_404(Perps, pk=pk)
    form = PerpCreate(request.POST or None, instance=perp)
    if form.is_valid():
        form.save()
        return redirect('/neighborhoodwatch/')
    return render(request, template_name, {'form': form})