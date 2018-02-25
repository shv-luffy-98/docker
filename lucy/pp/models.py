from django.db import models

# Create your models here.
class College(models.Model):
    college code = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 10)
    type = model.CharField(max_length = 10)