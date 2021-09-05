from django.db import models

# Create your models here.
# in this file we have created a task model to add tasks in our todo app.
# the main function of todo app is to add different tasks which we have to do and make our 
# priorities. 
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

