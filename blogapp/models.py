from django.db import models

# Create your models here.
class authorName(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length =100)
    email = models.EmailField(max_length = 100)
    content = models.TextField(null = True)

    def __str__(self):
        return self.firstName ,self.lastName, self.email