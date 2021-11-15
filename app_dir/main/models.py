from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now
import datetime

class Bookmarks(models.Model):
    createdAt = models.DateTimeField(
        default=datetime.datetime.today,
        editable=False
    )
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True, null=True)