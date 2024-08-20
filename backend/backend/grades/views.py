from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Grades
from .serializers import GradeSerializer
from users.permissions import IsTeacher



class CreateGradeView(generics.CreateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAdminUser, IsTeacher]


class ListGradeView(generics.ListAPIView):
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Grades.objects.filter(student=self.request.user, student__status="student")


class DeleteGradeView(generics.DestroyAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAdminUser, IsTeacher]




