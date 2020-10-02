from django.db import models
from django.contrib.auth.models import User

class Contributor_Profile(models.Model):
    Username = models.CharField(max_length=200, null=False)
    First_name = models.CharField(max_length=50, null=False)
    Last_name = models.CharField(max_length=50, null=False)
    Date_of_Birth = models.DateField
    Email = models.EmailField
    Phone = models.IntegerField
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    password = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.User.username} Profile'
# Create your models here.

