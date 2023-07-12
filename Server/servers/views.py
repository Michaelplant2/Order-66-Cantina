from django.http import JsonResponse
from .models import Server

def index(request):
    servers = Server.objects.order_by('hire_date')
    servers_arr = []
    for con in servers:
        server_dict = {
            "name": con.name,
            "description": con.description,
            "photo": str(con.photo),
            "is_mvp": con.is_mvp,
            "hire_date": con.hire_date,
        }
        servers_arr.append(server_dict)
    return JsonResponse(servers_arr, safe=False)