from django.db import models

# Create your models here.
class MenuItem(models.Model):
    item_name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    description = models.TextField(blank=True, null=True)
    
    @classmethod
    def create_menu_item(cls, item_name, price, description):
        menu_item = cls(item_name=item_name, price=price, description=description)
        menu_item.save()

    @classmethod
    def get_all_menu_items(cls):
        return cls.objects.all()
    
    @classmethod
    def get_menu_item(cls, item_name):
        return cls.objects.filter(item_name=item_name).first()
