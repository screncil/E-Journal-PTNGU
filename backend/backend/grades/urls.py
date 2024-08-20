from django.urls import path
from .views import ListGradeView, CreateGradeView, DeleteGradeView

urlpatterns = [
    path('', ListGradeView.as_view(), name='grades-list'),
    path('<int:grade_id>/delete', DeleteGradeView.as_view(), name='grades-delete'),
    path('create', CreateGradeView.as_view(), name='grades-create'),
]