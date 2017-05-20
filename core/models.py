from django.db import models

# Create your models here.
class TestData(models.Model):
    """model containing the test data"""
    desc=models.TextField(max_length=200)
    def __str__(self):
        """function to return the string representation of the model"""
        return self.desc
