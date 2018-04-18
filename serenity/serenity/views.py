from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#from django.forms import ModelForm

from clients.models import Clients
from neighborhoodwatch.models import Perps

@login_required
def index(request):
    latest_client_list = Clients.objects.order_by('-client_id').filter(status_id = 1)[:5]
    latest_perps_list = Perps.objects.order_by('-perp_id')[:5]
    template = loader.get_template('serenity/index.html')
    context = {
        'latest_client_list': latest_client_list,
        'latest_perps_list': latest_perps_list,
    }
    return HttpResponse(template.render(context, request))


def emp_login(request):
    username = request.POST['username']
    password = request.POST['password']
    template_fail = 'serenity/invalid_user.html'
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect('/')
    else:
        return redirect(request, template_fail)
