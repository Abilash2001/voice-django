from statistics import mode
from djongo import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=False,null=False)
    phone = models.TextField(blank=False,null=False,max_length=10)
    email = models.TextField(blank=False,null=False)
    password = models.TextField(blank=False,null=False)


