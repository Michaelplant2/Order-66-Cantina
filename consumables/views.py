from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Consumable


def index(request):
    consumables = Consumable.objects.order_by('name').filter(is_published=True)

    paginator = Paginator(consumables, 6)
    page = request.GET.get('page')
    paged_consumables = paginator.get_page(page)

    context = {
        'consumables': paged_consumables
    }
    
    return render(request, 'consumables/consumables.html', context)

def consumable(request, consumable_id):
    consumable = get_object_or_404(Consumable, pk=consumable_id)

    context = {
        'consumable': consumable
    }

    return render(request, 'consumables/consumable.html', context)