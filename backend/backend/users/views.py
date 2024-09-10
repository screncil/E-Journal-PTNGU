from django.contrib.auth import authenticate, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import RegisterStudentSerializer, TeacherSerializer, StudentSerializer
from .models import User
from .permissions import IsTeacher


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = StudentSerializer(user, many=False)
        return Response(serializer.data)


class ListStudentsView(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsTeacher]

    def get_queryset(self):
        query_set = User.objects.filter(status="student")
        group_id = self.request.query_params.get('group_id')
        if group_id is not None:
            query_set = query_set.filter(group__id=group_id)
        return query_set


class RegisterStudentView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterStudentSerializer
    permission_classes = (IsAdminUser,)


class RegisterTeacherView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAdminUser,)


class LoginUserAPIView(ObtainAuthToken):
    def post(self, request):
        if "username" not in request.data:
            return Response({"success": False, "msg": "Username field is null"})
        if "password" not in request.data:
            return Response({"success": False, "msg": "Password field is null"})

        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"success": True, "token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"success": False, "msg": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        

class LogoutUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"success": True})