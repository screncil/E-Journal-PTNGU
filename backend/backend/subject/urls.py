from django.urls import path

from views import ListSubjectView

urlpatterns = [
    path('', ListSubjectView.as_view(), name='subject-list'),
]