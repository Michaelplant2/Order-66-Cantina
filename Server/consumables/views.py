from django.http import JsonResponse
from .models import Consumable


def index(request):
    consumables = Consumable.objects.order_by('name').filter(is_published=True)
    consumables_arr = []
    for con in consumables:
        consumable_dict = {
            "name": con.name,
            "price": con.price,
            "description": con.description,
            "photo_main": str(con.photo_main),
            "cuisine_type": con.cuisine_type,
            "is_published": con.is_published,
        }
        consumables_arr.append(consumable_dict)
    return JsonResponse(consumables_arr, safe=False)