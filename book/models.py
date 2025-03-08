from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    car_number = models.CharField(max_length=50)
    services = models.JSONField(default=list, blank=True)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return f"Booking by {self.name} on {self.date}"

