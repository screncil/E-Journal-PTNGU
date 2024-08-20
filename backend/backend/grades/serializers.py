from rest_framework.serializers import ModelSerializer
from .models import Grades


class GradeSerializer(ModelSerializer):
    class Meta:
        model = Grades
        fields = ('id', 'grade', 'subject', 'theme', 'student')