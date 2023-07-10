from django.db import models

class Consumable(models.Model):
    FOOD = 'FD'
    DRINK = 'DR'
    CUISINE_TYPE = [
        (FOOD, 'Food'),
        (DRINK, 'Drink'),
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    cuisine_type = models.CharField(max_length=2, choices=CUISINE_TYPE)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name