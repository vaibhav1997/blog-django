from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class authorName(models.Model):
#     firstName = models.CharField(max_length = 100)
#     lastName = models.CharField(max_length =100)
#     email = models.EmailField(max_length = 100)
#     content = models.TextField(null = True)

#     def __str__(self):
#         return self.firstName ,self.lastName, self.email
    
# class user(models.User):
#     username = models.User(max_length=17)
#     first_name = models.User()
#     last_name = models.User(blank = True)
#     email = models.User()
#     password = models.User()
#     last_login = models.User()
#     date_joined = models.User()

class CustomUser(AbstractUser):


    def __str__(self):
        return self.email


