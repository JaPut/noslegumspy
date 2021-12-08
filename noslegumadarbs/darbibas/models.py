from django.db import models



class StudentModel(models.Model):

        name = models.CharField(max_length=77)
        grades = models.CharField(max_length=78)
        average_grade = models.CharField(max_length=78)