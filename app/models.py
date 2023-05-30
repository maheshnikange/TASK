from django.db import models

# Create your models here
c=(('completed','completed'),('pending','pending'))
class Task(models.Model):
    task_name=models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    due_date=models.DateField()
    status=models.CharField(max_length=20,choices=c)

    def __str__(self):
        return self.task_name
