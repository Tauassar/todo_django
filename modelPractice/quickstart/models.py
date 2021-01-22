from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.TextField()
    surname = models.TextField()

class Student(models.Model):
    name = models.TextField()
    surname = models.TextField()
    personal_tutor = models.ManyToManyField(
        Professor,
        related_name='tutoring'
    )
class Subject(models.Model):
    name = models.TextField()
