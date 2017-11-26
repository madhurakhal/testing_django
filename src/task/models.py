from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(verbose_name='Deu Date')
    complete_time = models.DateTimeField()


    def __str__(self):
        return self.title
