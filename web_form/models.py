from django.db import models

# Create your models here.
class User(models.Model):
    Full_name = models.CharField(max_length=30)
    Phone_number=models.IntegerField()
    Email_address=models.EmailField()
    Message=models.TextField()

    def __str__(self):
            return self.Full_name