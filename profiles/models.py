from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    email = models.EmailField(unique=True, max_length=254)
    profile_pic = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"