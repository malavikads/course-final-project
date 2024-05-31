from django.db import models

# Create your models here.
class Listtour(models.Model):
    name=models.CharField(max_length=100)
    departure_date=models.CharField(max_length=100)
    accomodation=models.CharField(max_length=100)
    transportation=models.CharField(max_length=100)
    duration=models.IntegerField()
    cost=models.IntegerField()
    activities=models.CharField(max_length=500)
    climate=models.CharField(max_length=100)

class Vendorf(models.Model):
    name_of_vendor=models.CharField(max_length=20)
    visiting_place=models.CharField(max_length=40)
    duration=models.IntegerField()
    departure_date=models.CharField(max_length=40)
    accomodation=models.CharField(max_length=40)
    transportation=models.CharField(max_length=40)
    contact_no=models.IntegerField()
