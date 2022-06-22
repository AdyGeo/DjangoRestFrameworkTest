from queue import Empty
from django.db import models

PRIORITY_CHOICES = [
    ('L','LOW'),
    ('M','MEDIUM'),
    ('H','HIGH')
]


class Task (models.Model):
    description = models.TextField(max_length=1000,null=False,blank=False)
    insdate = models.DateField("insert date", auto_now=False, auto_now_add=True)
    duedate = models.DateField("due date", null=True, blank=True)
    priority = models.CharField("prority",max_length=1,choices=PRIORITY_CHOICES,null=False, blank=False, default='M')
    done = models.BooleanField("completed",default=False)

    def __str__(self):
        return self.description


class Note (models.Model):
    title = models.CharField(max_length=100,null=False,blank=False)
    description = models.TextField(max_length=1000,null=False,blank=False)
    insdate = models.DateField("insert date", auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

