from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

""" Profile """
class Profile(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    funcList = (
        ('TIME_SERIES_INTRADAY','TIME_SERIES_INTRADAY'),
        ('TIME_SERIES_DAILY', 'TIME_SERIES_DAILY'),
        ('TIME_SERIES_ADJUSTED', 'TIME_SERIES_ADJUSTED'),
        ('TIME_SERIES_INTRADAY', 'TIME_SERIES_INTRADAY'),
        ('TIME_SERIES_WEEKLY', 'TIME_SERIES_WEEKLY'),
        ('TIME_SERIES_WEEKLY_ADJUSTED', 'TIME_SERIES_WEEKLY_ADJUSTED'),
        ('TIME_SERIES_MONTHLY', 'TIME_SERIES_MONTHLY'),
        ('TIME_SERIES_MONTHLY_ADJUSTED', 'TIME_SERIES_MONTHLY_ADJUSTED'),
        ('FX_INTRADAY', 'FX_INTRADAY'),
        ('FX_DAILY', 'FX_DAILY'),
        ('FX_WEEKLY', 'FX_WEEKLY'),
        ('FX_MONTHLY','FX_MONTHLY'),
        ('CURRENCY_DAILY', 'CURRENCY_DAILY'),
        ('CURRENCY_WEEKLY','CURRENCY_WEEKLY'),
        ('CURRENCY_MONTHLY','CURRENCY_MONTHLY')
    )
    function = models.CharField(max_length=50, choices=funcList)
    interval = models.IntegerField()
    fullOutputSize = models.BooleanField(default=False)
    autoUpdate = models.BooleanField(default=False)
    stocksUpdate = models.BooleanField(default=False)
    fxUpdate = models.BooleanField(default=False)




