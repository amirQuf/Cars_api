from django.db import models

from car_api.users.models import User

class Car(models.Model):
    name = models.CharField(max_length=40)
    number_of_cylinders = models.PositiveIntegerField()
    number_of_passengers = models.PositiveIntegerField()
    Cylinder_volume = models.FloatField() 
    color = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = [ "-modified","-created"]
    