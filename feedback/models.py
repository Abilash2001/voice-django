from unittest.util import _MAX_LENGTH
from djongo import models

class UserFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.TextField(blank=False,null=False)
    Email = models.TextField(blank=False,null=False)
    Star = models.CharField(max_length=1)
    Feedback = models.TextField(blank=False,null=False)
