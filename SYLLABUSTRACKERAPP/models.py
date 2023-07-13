from django.db import models

# Create your models here.

class course(models.Model):
    course=models.CharField(max_length=250)
    Active=models.BooleanField() 
    def __str__(self):
        return self.course

class day(models.Model):
    day=models.CharField(max_length=250)
    Active=models.BooleanField() 
    def __str__(self):
        return self.day


class syllabus(models.Model):
    syllabus=models.CharField(max_length=250)
    Active=models.BooleanField() 
    def __str__(self):
        return self.syllabus


class course_syllabus(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    day=models.ForeignKey(day,on_delete=models.CASCADE)
    syllabus=models.ForeignKey(syllabus,on_delete=models.CASCADE)



