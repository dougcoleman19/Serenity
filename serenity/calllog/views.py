from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

from .models import CallLog
from .forms import Call_Log_Create


@login_required
def index(request):
    latest_call_log_list = CallLog.objects.order_by('call_log_id')[:5]
    #latest_perps_list = Perps.objects.order_by('-perp_id').filter(status_id = 2)[:5]
    #clients_missing_number = Clients.objects.order_by('-client_id').exclude(client_number__contains="DV").exclude(client_number__contains="SA")[:5]
    template = loader.get_template('calllog/index.html')
    context = {
        'latest_call_log_list': latest_call_log_list,
        #'clients_missing_number': clients_missing_number,
        #'latest_perps_list': latest_perps_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def call_log_create(request):
    if request.method == "POST":
        form = Call_Log_Create(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/calllog/')
    else:
        form = Call_Log_Create()
    return render(request, 'calllog/new.html', {'form':form})


def calllogdetail(request, call_log_id):
    try:
        calllog = CallLog.objects.get(pk=call_log_id)
        context = {
            'calllog': calllog,
        }
        template = loader.get_template('calllog/detail.html')
    except CallLog.DoesNotExist:
        raise Http404("Call Log does not exist")
    return HttpResponse(template.render(context, request))


def call_log_update(request, pk, template_name='calllog/new.html'):
    calllog = get_object_or_404(CallLog, pk=pk)
    form = Call_Log_Create(request.POST or None, instance=calllog)
    if form.is_valid():
        form.save()
        return redirect('/call_log/')
    return render(request, template_name, {'form': form})