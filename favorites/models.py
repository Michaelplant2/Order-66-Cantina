from django.db import models
from django.conf import settings
from consumables.models import Consumable

class Favorite(models.Model):
    consumable_id = models.ForeignKey(Consumable, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.name