from rest_framework import serializers
from .models import User

from groups.serializers import GroupSerializer


class StudentSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'status', 'group', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

class RegisterStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'status', 'group')
        extra_kwargs = {'password': {'write_only': True}, 'group': {'required': True}}

    def create(self, validated_data):
        validated_data['status'] = 'student'
        user = User.objects.create_user(**validated_data)
        return user

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'status')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['status'] = 'teacher'
        user = User.objects.create_user(**validated_data)
        return user