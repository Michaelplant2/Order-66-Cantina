from django.db import models

class Favorite(models.Model):
    consumable_id = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name