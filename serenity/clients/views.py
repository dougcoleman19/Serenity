from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

from .models import Clients
from .forms import ClientInsertTest

from calllog.models import CallLog

@login_required

def index(request):
    latest_client_list = Clients.objects.order_by('-client_id').filter(status_id = 1)[:5]
    #latest_perps_list = Perps.objects.order_by('-perp_id').filter(status_id = 2)[:5]
    clients_missing_number = Clients.objects.order_by('-client_id').exclude(client_number__contains="DV").exclude(client_number__contains="SA")[:5]
    template = loader.get_template('clients/index.html')
    context = {
        'latest_client_list': latest_client_list,
        'clients_missing_number': clients_missing_number,
        #'latest_perps_list': latest_perps_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, client_id):
    try:
        client = Clients.objects.get(pk=client_id)
        #calllog = CallLog.objects.get(pk=client_id)
        context = {
            'client': client,
            #'calllog': calllog,
        }
        template = loader.get_template('clients/detail.html')
    except Clients.DoesNotExist:
        raise Http404("Client does not exist")
    return HttpResponse(template.render(context, request))
    #return render(request, 'clients/detail.html', {'client': client, 'calllog' : calllog, })


def client_create(request):
    if request.method == "POST":
        form = ClientInsertTest(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clients/')
    else:
        form = ClientInsertTest()
    return render(request, 'clients/forms.html', {'form':form})


def client_create_mini(request, template_name='clients/forms-mini.html'):
    form = ClientInsertTest(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/clients/new/success/')
    return render(request, template_name, {'form':form})


def client_update(request, pk, template_name='clients/forms.html'):
    client = get_object_or_404(Clients, pk=pk)
    form = ClientInsertTest(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('/clients/')
    return render(request, template_name, {'form': form})


def information_received(request):
    return HttpResponse("<p>Client information successfully uploaded. Please close this window and refresh the call log page.</p>")


@permission_required('clients.can_delete', raise_exception="true")
def client_delete(request, pk, template_name='clients/client_confirm_delete.html'):
    template_fail = 'clients/invalid_permissions.html'
    client = get_object_or_404(Clients, pk=pk)
    if request.method=='POST':
        client.delete()
        return redirect('/clients')
    else:
        return redirect(request, template_fail)
    return render(request, template_name, {'object':client})


def emp_login(request):
    username = request.POST['username']
    password = request.POST['password']
    template_fail = 'clients/invalid_user.html'
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect('/')
    else:
        return redirect(request, template_fail)


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")


