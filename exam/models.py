from django.db import models


# Create your models here.
class Stack(models.Model):
    stack_data = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stack_data
