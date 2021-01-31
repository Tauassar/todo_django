from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.TextField()
    surname = models.TextField()
    def __str__(self):
        return self.name+" "+self.surname

class Student(models.Model):
    name = models.TextField()
    surname = models.TextField()
    personal_tutor = models.OneToOneField(
        Professor,
        on_delete=models.CASCADE,
        related_name='tutoring'
    )
    def __str__(self):
        return self.name+" "+self.surname

class Subject(models.Model):
    name = models.TextField()
