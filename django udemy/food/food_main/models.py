from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    
    def __str__(self):
        connector = "an" if self.item_desc[0].lower() in ['a','e','i','o','u'] else "a"
        return f'{self.item_name} is {connector} {self.item_desc}'