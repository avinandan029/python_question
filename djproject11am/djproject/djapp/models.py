from django.db import models

class RegistrationData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)


