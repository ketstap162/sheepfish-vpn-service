from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Site(models.Model):
    url = models.URLField()
    alias = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    objects = models.Manager()
