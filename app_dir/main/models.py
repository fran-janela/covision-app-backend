from datetime import datetime
from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now
import datetime

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateField(
        default=datetime.date.today,
        editable=False
    )
    cases = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)