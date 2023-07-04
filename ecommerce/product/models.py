from django.db import models

# Create your models here.
class product(models.Model):
  productname=models.CharField(max_length=20)
  datecurrent=models.CharField(max_length=20)
  

  def __str__(self):
        return self.productname