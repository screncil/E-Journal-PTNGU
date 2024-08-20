from rest_framework.serializers import ModelSerializer, RelatedField

from .models import Grades
from users.models import User


class GradeSerializer(ModelSerializer):
    class Meta:
        model = Grades
        fields = ('id', 'grade', 'theme', 'student', 'subject')
        extra_kwargs = {'student': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        return Grades.objects.create(**validated_data)