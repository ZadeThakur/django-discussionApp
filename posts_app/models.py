from django.db import models
from django.utils import timezone
# Create your models here.
class postsModel(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=30,null=False)
    log = models.CharField(max_length=1000,null=False)

    def __str__(self):
        return self.name