from django.contrib.auth.models import User
from django.db import models


class UserModel(models.Model):
    covid_positive = models.BooleanField(default=False)
    covid_contact = models.BooleanField(default=False)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    friends = models.ManyToManyField('self')


