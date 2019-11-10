from django.db import models


class Course(models.Model):

    courseName = models.CharField(max_length=100)
    courseHourse = models.IntegerField(default=3)

    def __str__(self):
        return self.courseName


class Student(models.Model):

    studentName = models.CharField(max_length=200)
    studentDateOfBirth = models.DateField()
    studentStatus = models.CharField(max_length=50)
    studentGPA = models.FloatField()

    def __str__(self):
        return self.studentName


class Enroll(models.Model):

    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    couesePractical = models.IntegerField(default=0)
    courseYearWork = models.IntegerField(default=0)
    finalExamAbsent = models.BooleanField()
    finalExamScore = models.FloatField()
    courseTotalScore = models.FloatField()

    def __str__(self):
        return str(self.studentID) + ' in ' + str(self.courseID)
