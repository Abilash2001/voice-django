from djongo import models
class UserFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    Email = models.TextField(blank=False,null=False)
    Feedback = models.TextField(blank=False,null=False)
