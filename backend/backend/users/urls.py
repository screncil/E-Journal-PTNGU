from django.urls import path

from .views import RegisterTeacherView, RegisterStudentView, LoginUserAPIView, LogoutUserView, ListStudentsView, UserProfileView

urlpatterns = [
    path("student/all", ListStudentsView.as_view(), name="all-students"),
    path("student/register", RegisterStudentView.as_view(), name="register-student"),
    path("teacher/register", RegisterTeacherView.as_view(), name="teacher-register"),
    path("login", LoginUserAPIView.as_view(), name="user-login"),
    path("logout", LogoutUserView.as_view(), name="user-logout"),
    path("me", UserProfileView.as_view(), name="user-profile"),
]