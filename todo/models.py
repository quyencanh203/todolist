from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    done = models.BooleanField()
    
    def __str__(self) -> str:
        return self.title

