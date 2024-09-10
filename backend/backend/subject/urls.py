from django.urls import path

from .views import ListSubjectView, CreateSubjectView, DeleteSubjectView

urlpatterns = [
    path('', ListSubjectView.as_view(), name='subject-list'),
    path('/<int:pk>/delete', DeleteSubjectView.as_view(), name='subject-delete'),
    path('/create', CreateSubjectView.as_view(), name='subject-create')
]