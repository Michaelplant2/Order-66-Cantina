from django.shortcuts import render
from consumables.models import Consumable
from servers.models import Server

def index(request):
    consumables = Consumable.objects.all().filter(is_published=True)
    servers = Server.objects.order_by('-hire_date')
    mvp_servers = Server.objects.all().filter(is_mvp=True)

    context = {
        'consumables': consumables,
        'servers': servers,
        'mvp_servers': mvp_servers,
    }

    return render(request, 'pages/index.html', context)