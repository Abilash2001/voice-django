from django.db import models

# Create your models here.
from djongo import models

class UserQuery(models.Model):
    id = models.AutoField(primary_key=True)
    mobile_no = models.TextField(blank=False,null=False)
    Email = models.TextField(blank=False,null=False)
    a = models.CharField(max_length=1)
    Query = models.TextField(blank=False,null=False)
