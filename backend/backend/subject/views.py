from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from .models import Subjects
from subject.serializers import SubjectSerializer
from users.permissions import IsTeacher


class ListSubjectView(ListAPIView):
    serializer_class = SubjectSerializer
    permission_classes = [IsTeacher, IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = Subjects.objects.all()
        course = self.request.query_params.get('course')

        if course is not None:
            queryset = queryset.filter(course=course)
        return queryset


class CreateSubjectView(CreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsTeacher, IsAdminUser]
    authentication_classes = [TokenAuthentication]


class DeleteSubjectView(DestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsTeacher, IsAdminUser]
    authentication_classes = [TokenAuthentication]
