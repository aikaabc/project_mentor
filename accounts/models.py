from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Mentor(models.Model):
    user = models.OneToOneField(User, related_name='mentor', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='mentors')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'