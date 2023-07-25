from django.db import models

class Consumable(models.Model):
    FOOD = 'FD'
    DRINK = 'DR'
    CUISINE_TYPE = [
        (FOOD, 'Food'),
        (DRINK, 'Drink'),
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    cuisine_type = models.CharField(max_length=2, choices=CUISINE_TYPE)
    is_published = models.BooleanField(default=True)