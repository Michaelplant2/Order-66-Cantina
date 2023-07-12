from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='consumables'),
    path('<int:consumable_id>', views.consumable, name='consumable'),
    path('search', views.search, name='search'),
]