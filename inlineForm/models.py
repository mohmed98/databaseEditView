from django.db import models


class CourseScore(models.Model):
    name = models.CharField(max_length=50)
    studentName = models.CharField(max_length=50)
    score = models.IntegerField(default="0")

    def __str__(self):
        return self.name
