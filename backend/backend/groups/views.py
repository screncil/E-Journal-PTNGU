from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

from .models import Group
from .serializers import GroupSerializer

from users.permissions import IsTeacher
from rest_framework.permissions import IsAdminUser


# Create your views here.

class GroupListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser, IsTeacher]
    authentication_classes = (TokenAuthentication,)


class AddGroupView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = (TokenAuthentication,)


class DeleteGroupView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = (TokenAuthentication,)
