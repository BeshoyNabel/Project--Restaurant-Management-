from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
    class Meta:
        unique_together = ('name', 'phone')
    
    @classmethod
    def getallcustomer(cls):
        return cls.objects.all().order_by('id')

    @classmethod
    def getcustomer(cls, name, phone):
        return cls.objects.get(name=name, phone=phone)
    
    @classmethod
    def createcustomer(cls, name, phone, email):
        cls.objects.create(name=name, phone=phone, email= email)
        
    @classmethod
    def sortcustomerbyname(cls, sort):
        if sort == 'Desc':
            return cls.objects.all().order_by('name')
        elif sort == 'Asc':
            return cls.objects.all().order_by('-name')
        
