from django.db import models
from django.contrib.auth.models import AbstractUser

from groups.models import Group




class User(AbstractUser):
    CHOICES = (
        ("student", "Студент"),
        ("teacher", "Викладач")
    )
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    status = models.CharField(choices=CHOICES, null=True, blank=True, max_length=20)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_teacher(self):
        return self.status == "teacher"
