from django.shortcuts import render
from carpoolhost.models import Member,RegMember,Host,Client
from django.views import generic
# Create your views here.

def index(request):
    num_hosts = Host.objects.all().count()
    num_clients=Client.objects.all().count()
    context={
        'num_hosts' : num_hosts,
        'num_clients' : num_clients,
    }
    return render(request, 'index.html',context=context)

class HostListView(generic.ListView):
    model = Host
