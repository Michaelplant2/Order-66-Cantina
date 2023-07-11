from django.http import JsonResponse


from .models import Consumable


def index(request):
    consumables = Consumable.objects.order_by('name').filter(is_published=True)
    dict = {
        Consumable
    }

    return JsonResponse(request, dict)