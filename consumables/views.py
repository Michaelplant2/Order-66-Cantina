from django.shortcuts import get_object_or_404, render
from .models import Consumable
from favorites.models import Favorite


def index(request):
    consumables = Consumable.objects.order_by('name').filter(is_published=True)

    context = {
        'consumables': consumables
    }
    
    return render(request, 'consumables/consumables.html', context)

def consumable(request, consumable_id):

    consumable = get_object_or_404(Consumable, pk=consumable_id)
    
    favored = request.GET.get('favorite', 'false');

    if favored != "false":
        fav_consumable = Favorite(consumable_id=consumable, user_id=request.user);
        fav_consumable.save()

    context = {
        'consumable': consumable
    }

    return render(request, 'consumables/consumable.html', context)