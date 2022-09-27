
from djongo import models

class Dongleplans(models.Model):
    id = models.AutoField(primary_key=True)
    plan_price = models.TextField(blank=False,null=False)
    plan_data = models.TextField(blank=False,null=False)
    plan_validity = models.TextField(blank=False,null=False)
    plan_usage = models.IntegerField(blank=False,null=False)