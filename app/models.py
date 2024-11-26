from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Collector(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='m@gmail.com')
import uuid
class WasteCollectionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_id = models.AutoField(primary_key=True)


    collection_date = models.DateField()
    collection_time = models.TimeField()
    address = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Scheduled', 'Scheduled'), ('Completed', 'Completed')], default='Pending')

