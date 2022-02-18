from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Customer(models.Model):
    gender = models.CharField(max_length=225, null=True, blank=True)
    contact = models.CharField(max_length=225, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)


class Flight(models.Model):
    airline = models.CharField(max_length=225, null=True, blank=True)
    registration_no = models.CharField(max_length=225, null=True, blank=True)
    plain_model = models.CharField(max_length=225, null=True, blank=True)
    available_seats = models.IntegerField(default=0, null=True, blank=True)
    from_country = models.CharField(max_length=225, null=True, blank=True)
    destination = models.CharField(max_length=225, null=True, blank=True)
    ticket_num = models.CharField(max_length=225, null=True, blank=True)
    date_avail = models.DateField(null=True, blank=True)
    date_flight = models.DateField(null=True, blank=True)
    time_depart = models.CharField(max_length=225, null=True, blank=True)
    time_land = models.CharField(max_length=225, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.airline


class Booking(models.Model):
    cust_ID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    flight_ID = models.ForeignKey(Flight, on_delete=models.SET_NULL, null=True)
    date_reserve = models.DateField(null=True, blank=True)
    date_cancel = models.DateField(null=True, blank=True)
    is_canceled = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.cust_ID
