from statistics import mode
from djongo import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=False,null=False)
    phone = models.TextField(blank=False,null=False,max_length=10)
    email = models.TextField(blank=False,null=False)
    password = models.TextField(blank=False,null=False)
    isAdmin = models.BooleanField(blank=False,null=False)


class Phone(models.Model):
    id =  models.AutoField(primary_key=True)
    phoneNo = models.TextField(blank=False,null=False)
    hashPhone = models.TextField(blank=False,null=False)
    register = models.BooleanField(blank=False,null=False)
    userId  = models.IntegerField()


class UsersDetails(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.IntegerField(blank=False,null=False)
    userCat = models.CharField(max_length=1,blank=False,null=False)
    joined = models.DateTimeField(auto_created=True,auto_now_add=True,blank=False,null=False)
    