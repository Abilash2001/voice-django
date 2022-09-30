from django.db import models

# Create your models here.
from djongo import models


class Postpaidplan(models.Model):
    id = models.AutoField(primary_key=True)
    plan_price = models.TextField(blank=False, null=False)
    plan_talktime = models.TextField(blank=False, null=False)
    plan_data = models.TextField(blank=False, null=False)
    plan_usage = models.IntegerField(blank=False, null=False)