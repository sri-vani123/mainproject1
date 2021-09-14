from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Attendance(models.Model):
    StudentName = models.CharField(max_length=200, null=True)
    StudentId = models.CharField(max_length=50, null=True)
    LecturesAttended = models.IntegerField(null=True)
    TotalLectures = models.IntegerField(null=True)

    def __str__(self):
        return self.StudentName