from django.db import models

# Create your models here.
class mails(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, null= True)
    email=models.EmailField(max_length=80,null= True)
    message=models.TextField(null= True)