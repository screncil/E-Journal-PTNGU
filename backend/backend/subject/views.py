from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from .models import Subjects
from subject.serializers import SubjectSerializer
from users.permissions import IsTeacher


class ListSubjectView(ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subjects.objects.all()
    permission_classes = [IsTeacher, IsAdminUser]
    authentication_classes = [TokenAuthentication]
