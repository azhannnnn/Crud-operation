from django.db import models

# asdfghjklpoiuytrewqzxcvbnm
class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

class Query(models.Model):
    Email = models.EmailField()
    query = models.CharField(max_length=100)

