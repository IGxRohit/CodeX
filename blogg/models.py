from django.db import models

# Create your models here.
class contactUs (models.Model):
    username=models.CharField( max_length=150)
    email=models.EmailField( max_length=254)
    phone=models.IntegerField()
    message=models.TextField()
    myimage = models.ImageField(upload_to = "userprofile", null = True, blank = True)
