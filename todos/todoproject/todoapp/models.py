from django.db import models


class task(models.Model):
    name=models.CharField(max_length=250,null=True)
    priority=models.IntegerField()
    date=models.DateField(null=True)
    def __str__(self):
     return self.name