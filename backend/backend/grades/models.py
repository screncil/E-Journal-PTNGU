from django.db import models
from django.utils import timezone

from subject.models import Subjects
from users.models import User

# Create your models here.



class Grades(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.IntegerField(null=False, blank=False)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    theme = models.TextField()
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'status': 'student'},
    )
    date = models.DateField()