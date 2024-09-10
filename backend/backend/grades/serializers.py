from rest_framework.serializers import ModelSerializer

from .models import Grades
from users.serializers import StudentSerializer


class CreateGradeSerializer(ModelSerializer):
    class Meta:
        model = Grades
        fields = ('id', 'grade', 'theme', 'student', 'subject', 'date')
        extra_kwargs = {'student': {'required': True, 'write_only': True}, 'date': {'required': True}}

    def create(self, validated_data):
        return Grades.objects.create(**validated_data)


class GradeSerializer(ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:
        model = Grades
        fields = ('id', 'grade', 'theme', 'subject', 'student')
        extra_kwargs = {'student': {'read_only': True}}