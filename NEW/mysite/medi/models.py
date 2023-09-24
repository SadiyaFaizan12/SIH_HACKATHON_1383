from django.db import models
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

def __str__(self):
    return self.name

# Create your models here.
