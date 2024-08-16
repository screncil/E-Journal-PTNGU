from django.contrib.auth import authenticate, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import StudentSerializer, TeacherSerializer
from .models import User
from .permissions import IsTeacher


class ListStudentsView(generics.ListAPIView):
    queryset = User.objects.filter(status="student")
    serializer_class = StudentSerializer
    permission_classes = [IsTeacher]


class RegisterStudentView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentSerializer
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