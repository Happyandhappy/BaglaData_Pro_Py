from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Alpha_Vantage_Settings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apiKey = models.CharField(max_length=100)                          # Api Key
    symbolListProfiles = models.BooleanField(default=False)            # Symbol list profiles
    isProfile = models.BooleanField(default=False)



