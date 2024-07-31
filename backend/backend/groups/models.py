from django.db import models

# Create your models here.


class Group(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    course = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
