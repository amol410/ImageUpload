from django.db import models


# Create your models here, storing the data
# Upload_to is parameter here
class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)

# This is second thing after settings you can do makemigrations and migrate once you register it with admin
# then create superuser
