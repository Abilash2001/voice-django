# Create your models here.
from tokenize import blank_re
from djongo import models

class UserQuery(models.Model):
    id = models.AutoField(primary_key=True)
    mobile_no = models.TextField(blank=False,null=False)
    Email = models.TextField(blank=False,null=False)
    a = models.CharField(max_length=1)
    admin_name = models.TextField(blank=False,null=False)
    admin_id = models.IntegerField()
    Query = models.TextField(blank=False,null=False)
