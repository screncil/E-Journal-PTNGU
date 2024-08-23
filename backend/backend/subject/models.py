from django.db import models

# Create your models here.


class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    course = models.IntegerField()
    specializtion = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
